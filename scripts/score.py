import requests

API_KEY = "Os8Fxo5yxnt6TB0zzt_HAs0ZhKF5sf1Oo_rCinsZPFg8"

# Get the IAM token
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token',
    data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
)
mltoken = token_response.json()["access_token"]

# Prepare the header
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# Sample input data: replace with actual feature names and values
payload_scoring = {
    "input_data": [
        {
            "fields": ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment", "urgent", "hot",
                       "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
                       "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login", "count", "srv_count",
                       "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
                       "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
                       "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
                       "dst_host_rerror_rate", "dst_host_srv_rerror_rate"],
            "values": [[0, "tcp", "http", "SF", 181, 5450, 0, 0, 0, 0,
                        0, 1, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 9, 9,
                        0.00, 0.00, 0.00, 0.00, 1.00, 0.00,
                        0.00, 9, 9, 1.00, 0.00,
                        0.11, 0.00, 0.00, 0.00,
                        0.00, 0.00]]
        }
    ]
}

# Replace this with your actual deployment URL
scoring_url = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/8e7f0b95-089d-47e1-82b9-f6aebb172b24/predictions?version=2021-05-01"

response = requests.post(scoring_url, json=payload_scoring, headers=header)

print("Scoring response:")
print(response.json())
