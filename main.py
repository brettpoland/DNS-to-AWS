from xml import dom
import boto3
import csv
import whois
import argparse
import json

def read_csv(csvfile):
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dns_info = []
        dns_list=[]

        
        for dns_info in csv_reader:
            dns_info.append(dns_info)
            w = dns_info[0]
            y = dns_info[1]
            dns_list.append([w,y])
        return dns_list

def whois_dns(address):
        x = whois.whois(address)
        print (x)  
         
def getall_aws_dns():
        client = boto3.client('route53domains', region_name='us-east-1')
        response = client.list_domains()
        for domain in response:
            set_dns_contact (response["DomainName"])

def set_dns_contact(domain):
    client = boto3.client('route53domains', region_name='us-east-1')
    response = client.update_domain_contact(
    DomainName=domain,
    AdminContact={
        'FirstName': 'string',
        'LastName': 'string',
        'ContactType': 'string',
        'OrganizationName': 'string',
        'AddressLine1': 'string',
        'AddressLine2': '',
        'City': 'string',
        'State': 'string',
        'CountryCode': 'string',
        'ZipCode': 'string',
        'PhoneNumber': '+string',
        'Email': 'string',
    },
    RegistrantContact={
        'FirstName': 'string',
        'LastName': 'string',
        'ContactType': 'string',
        'OrganizationName': 'string',
        'AddressLine1': 'string',
        'AddressLine2': '',
        'City': 'string',
        'State': 'string',
        'CountryCode': 'string',
        'ZipCode': 'string',
        'PhoneNumber': '+string',
        'Email': 'string',
    },
    TechContact={
        'FirstName': 'string',
        'LastName': 'string',
        'ContactType': 'string',
        'OrganizationName': 'string',
        'AddressLine1': 'string',
        'AddressLine2': '',
        'City': 'string',
        'State': 'string',
        'CountryCode': 'string',
        'ZipCode': 'string',
        'PhoneNumber': '+string',
        'Email': 'string',
    },
    )
    print(response)
            
def route_53_transfer(address, code):
    client = boto3.client('route53domains', region_name='us-east-1')
    response = client.transfer_domain(
    DomainName=address,
    DurationInYears=1,
    AuthCode=code,
    AutoRenew=True,
    AdminContact={
        'FirstName': 'string',
        'LastName': 'string',
        'ContactType': 'string',
        'OrganizationName': 'string',
        'AddressLine1': 'string',
        'AddressLine2': '',
        'City': 'string',
        'State': 'string',
        'CountryCode': 'string',
        'ZipCode': 'string',
        'PhoneNumber': '+string',
        'Email': 'string',
    },
    RegistrantContact={
        'FirstName': 'string',
        'LastName': 'string',
        'ContactType': 'string',
        'OrganizationName': 'string',
        'AddressLine1': 'string',
        'AddressLine2': '',
        'City': 'string',
        'State': 'string',
        'CountryCode': 'string',
        'ZipCode': 'string',
        'PhoneNumber': '+string',
        'Email': 'string',
    },
    TechContact={
        'FirstName': 'string',
        'LastName': 'string',
        'ContactType': 'string',
        'OrganizationName': 'string',
        'AddressLine1': 'string',
        'AddressLine2': '',
        'City': 'string',
        'State': 'string',
        'CountryCode': 'string',
        'ZipCode': 'string',
        'PhoneNumber': '+string',
        'Email': 'string',
    },
    PrivacyProtectAdminContact=False,
    PrivacyProtectRegistrantContact=True,
    PrivacyProtectTechContact=True
    )
    print(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', type=str, required=False)
    parser.add_argument('-normalize', action='store_true', required=False)
    args = parser.parse_args()
    if args.normalize == True:
        print("Changing all aws account dns info.....")
        print(getall_aws_dns())
    else:
        urls = read_csv(args.csv)
        for i in urls:
            www = i[0]
            id = i[1]
            whois_dns(i[0])
            print("Code:" + id)
            reply =  input("Would you like to transfer this domain? (only 'Yes' accepted): ")
            if reply == "Yes":
                print ("Attempting transfer..... \n")
                route_53_transfer(www, id)
            else:
                print("DNS Not Transferred")
            
        
    
    