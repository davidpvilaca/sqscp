# SQSCP

Copy messages from one SQS queue to another and remove from the source if necessary.

## Prerequisites

* Python 2.7
* Pip 9

## Quickstart

1. Install requirements: `pip install -r requirements.txt`
2. Setup environments variables: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` (`AWS_SECURITY_TOKEN `, `AWS_PROFILE` optionals)
3. Run application: `python sqscp.py --src <source> --dst <destination> [options]`

## CLI

| Argument | Alias | Description |
|----|----|----|
| --src | -s | The source SQS queue. |
| --dst | -d | The destination SQS queue. |
| --region | - | AWS Region (default: us-east-1) |
| --remove | - | Flag to remove messages from the source queue. (default: false) |

## Usage example

```bash
python sqscp.py --src source_queue --dst destination_queue --region us-east-2
```
