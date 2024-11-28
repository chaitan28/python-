import json
import boto3
import string
import random

def lambda_handler(event, context):
    try:
    
        N = 14
        newpassword = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

        
        client = boto3.client('secretsmanager')

        
        secret_id = 'Chaitu_dev'  
        get_res = client.get_secret_value(SecretId=secret_id)
        current_secrets = json.loads(get_res['SecretString'])

        
        current_secrets.update({
            "Secret access key": newpassword,
            "Access key": newpassword,
        })

       
        response = client.put_secret_value(
            SecretId=secret_id,
            SecretString=json.dumps(current_secrets)
        )

        print(f"Updated secret successfully: {response}")
        return {
            'statusCode': 200,
            'body': json.dumps('Secret rotation completed successfully!')
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
