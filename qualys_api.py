import requests
from requests.auth import HTTPBasicAuth
from models import db, Vulnerability
from flask import current_app

QUALYS_API_URL = "https://qualysapi.qualys.com"

class QualysAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(self.username, self.password)

    def get_vulnerabilities(self):
        """
        Fetch vulnerabilities from Qualys API.
        This assumes Qualys returns a list of vulnerabilities in a report.
        """
        url = f"{QUALYS_API_URL}/api/2.0/fo/asset/host/vm/detection/"
        params = {
            'action': 'list',
            'output_format': 'json',
        }

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            current_app.logger.error(f"Error fetching vulnerabilities from Qualys API: {e}")
            return None

    def import_vulnerabilities(self, data):
        """
        Parse the Qualys data and save it to the database.
        """
        if data is None:
            current_app.logger.error("No data received from Qualys API.")
            return

        vulnerabilities = data.get('HOST_LIST_VM_DETECTION_OUTPUT', {}).get('RESPONSE', {}).get('HOST_LIST', [])

        for host in vulnerabilities:
            detections = host.get('DETECTION_LIST', {}).get('DETECTION', [])
            for detection in detections:
                cve_id = detection.get('QID')  # Assuming QID maps to a vulnerability identifier
                severity = detection.get('SEVERITY_LEVEL', 'Unknown')
                description = detection.get('VULN_DESCRIPTION', 'No description')

                # Check if the vulnerability already exists to prevent duplicates
                existing_vuln = Vulnerability.query.filter_by(cve_id=cve_id).first()
                if not existing_vuln:
                    vuln = Vulnerability(
                        cve_id=cve_id,
                        severity=severity,
                        description=description
                    )
                    db.session.add(vuln)
        
        db.session.commit()
        current_app.logger.info("Imported vulnerabilities from Qualys API.")

