import requests

NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def fetch_cves(keyword):
    print("\n[*] Fetching CVEs from NVD...\n")

    params = {
        "keywordSearch": keyword,
        "resultsPerPage": 5
    }

    response = requests.get(NVD_API_URL, params=params)

    if response.status_code != 200:
        print("[ERROR] Unable to fetch CVE data")
        return

    data = response.json()

    vulnerabilities = data.get("vulnerabilities", [])

    if not vulnerabilities:
        print("[SAFE] No CVEs found for this keyword")
        return

    for vuln in vulnerabilities:
        cve = vuln["cve"]
        cve_id = cve["id"]
        description = cve["descriptions"][0]["value"]

        print(f"[CVE FOUND] {cve_id}")
        print(f"Description: {description}")
        print("-" * 60)

if __name__ == "__main__":
    keyword = input("Enter software/service name (e.g. apache, openssl): ")
    fetch_cves(keyword)
