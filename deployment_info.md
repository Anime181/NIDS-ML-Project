
# 🛰 Deployment Information

This file contains details about the deployment of the Network Intrusion Detection System (NIDS) model using IBM Cloud AutoAI.

---

## 📍 Deployment Details

- **Model Name**: Network Intrusion Detection (AutoAI)
- **Deployment Name**: NIDS-Classifier
- **Deployment Platform**: IBM Watson Machine Learning
- **Deployment Type**: Online / REST API
- **Deployment Region**: au-syd
- **Version**: 2021-05-01

---

## 🌐 Scoring Endpoint

```
https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/8e7f0b95-089d-47e1-82b9-f6aebb172b24/predictions?version=2021-05-01
```

---

## 🔐 Authentication

This deployment uses **IBM IAM Token-based authentication**.

- You must obtain a token using your API key:
```python
import requests
response = requests.post(
    'https://iam.cloud.ibm.com/identity/token',
    data={"apikey": "your-ibm-api-key", "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
)
mltoken = response.json()["access_token"]
```

---

## 📦 Sample Input Format

```json
{
  "input_data": [
    {
      "fields": ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "..."],
      "values": [[0, 1, 4, 0, 181, 5450, "..."]]
    }
  ]
}
```

---

## 📈 Output Format

```json
{
  "predictions": [
    {
      "fields": ["prediction"],
      "values": [["normal"]]
    }
  ]
}
```

---

## 🛠 Dependencies

- IBM Cloud AutoAI
- IBM Watson Machine Learning
- Python 3.x
- Requests library

---

## ✍️ Author

- Animesh Gawhale
- Date: August 2025
