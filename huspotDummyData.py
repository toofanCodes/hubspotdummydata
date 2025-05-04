import csv
import random
import datetime
from faker import Faker
import uuid

numCompanies = 200
numContacts = 950
numDeals = 500
numTickets = 300
numActivities = 2000

lifecycleStages = ['Subscriber', 'Lead', 'Marketing Qualified Lead', 'Sales Qualified Lead', 'Opportunity', 'Customer', 'Evangelist', 'Other']
leadStatuses = ['New', 'Open', 'In Progress', 'Open Deal', 'Unqualified', 'Attempted to Contact', 'Connected', 'Bad Timing', None]
industries = ['Technology', 'Finance', 'Healthcare', 'Manufacturing', 'Retail', 'Education', 'Non-profit', 'Professional Services', 'Other']
dealStages = ['Appointment Scheduled', 'Qualified to Buy', 'Presentation Scheduled', 'Decision Maker Bought-In', 'Contract Sent', 'Closed Won', 'Closed Lost']
dealPipelines = ['Sales Pipeline', 'Renewals Pipeline']
dealTypes = ['New Business', 'Existing Business']
closedLostReasons = ['Price', 'Timing', 'Competitor', 'Lost Interest', 'Product Fit', None]
ticketStatuses = ['New', 'Waiting on contact', 'Waiting on us', 'Closed']
ticketPipelines = ['Support Pipeline', 'Onboarding Pipeline']
ticketPriorities = ['Low', 'Medium', 'High', 'Urgent']
ticketSources = ['Email', 'Phone', 'Chat', 'Form', 'Social Media']
activityTypes = ['Email', 'Call', 'Meeting', 'Note', 'Task']
callOutcomes = ['Connected', 'Left Voicemail', 'No Answer', 'Wrong Number', None]
meetingOutcomes = ['Scheduled', 'Completed', 'Rescheduled', 'No Show', 'Cancelled', None]
taskStatuses = ['Not Started', 'In Progress', 'Completed', 'Waiting', 'Deferred', None]

owners = ['dwight.schrute@example.com', 'michael.scott@example.com', 'pam.beesly@example.com', 'jim.halpert@example.com', 'angela.martin@example.com']
supportOwners = ['oscar.martinez@example.com', 'kevin.malone@example.com']
allOwners = owners + supportOwners

fake = Faker()
companiesData = []
contactsData = []
dealsData = []
ticketsData = []
activitiesData = []

def generateRandomDate(startDate=datetime.date(2022, 1, 1), endDate=datetime.date.today()):
    timeBetweenDates = endDate - startDate
    daysBetweenDates = timeBetweenDates.days
    if daysBetweenDates <= 0:
        return startDate
    randomNumberOfDays = random.randrange(daysBetweenDates) if daysBetweenDates > 0 else 0
    randomDate = startDate + datetime.timedelta(days=randomNumberOfDays)
    return randomDate

def writeToCsv(data, filename, fieldnames):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            if data:
                validFieldnames = [f for f in fieldnames if f in data[0]]
            else:
                validFieldnames = fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=validFieldnames)
            writer.writeheader()
            for row in data:
                filteredRow = {k: v for k, v in row.items() if k in validFieldnames}
                writer.writerow(filteredRow)
        print(f"Successfully generated {filename}")
    except Exception as e:
        print(f"Error writing {filename}: {e}")

print("Generating Companies...")
companyFieldnames = [
    'Company ID', 'Company Name', 'Company Domain Name', 'Industry',
    'Number of Employees', 'Annual Revenue', 'Phone Number', 'Website',
    'Street Address', 'City', 'State/Region', 'Postal Code', 'Country',
    'Create Date', 'Last Modified Date', 'Company Owner'
]
numSalesOwners = len(owners) if owners else 1
for i in range(numCompanies):
    companyId = f"COMP-{uuid.uuid4()}"
    domainName = fake.unique.domain_name()
    createDate = generateRandomDate()
    lastModifiedDate = generateRandomDate(startDate=createDate)
    companyOwner = owners[i % numSalesOwners] if owners else "default.owner@example.com"
    company = {
        'Company ID': companyId,
        'Company Name': fake.company(),
        'Company Domain Name': domainName,
        'Industry': random.choice(industries),
        'Number of Employees': random.randint(1, 10000),
        'Annual Revenue': round(random.uniform(50000, 50000000), 2),
        'Phone Number': fake.phone_number(),
        'Website': f"https://{domainName}",
        'Street Address': fake.street_address(),
        'City': fake.city(),
        'State/Region': fake.state_abbr(),
        'Postal Code': fake.zipcode(),
        'Country': fake.country(),
        'Create Date': createDate.isoformat(),
        'Last Modified Date': lastModifiedDate.isoformat(),
        'Company Owner': companyOwner
    }
    companiesData.append(company)
fake.unique.clear()

print("Generating Contacts...")
contactFieldnames = [
    'Contact ID', 'First Name', 'Last Name', 'Email', 'Phone Number',
    'Mobile Phone Number', 'Job Title', 'Lifecycle Stage', 'Lead Status',
    'Create Date', 'Last Modified Date', 'Contact Owner', 'Lead Source',
    'Website URL', 'Street Address', 'City', 'State/Region', 'Postal Code',
    'Country', 'Associated Company Domain'
]
companyDomains = [c['Company Domain Name'] for c in companiesData]
for i in range(numContacts):
    contactId = f"CONT-{uuid.uuid4()}"
    firstName = fake.first_name()
    lastName = fake.last_name()
    createDate = generateRandomDate()
    lastModifiedDate = generateRandomDate(startDate=createDate)
    lifecycleStage = random.choice(lifecycleStages)
    leadStatus = random.choice(leadStatuses) if lifecycleStage in ['Lead', 'Marketing Qualified Lead', 'Sales Qualified Lead'] else None
    contactOwner = owners[i % numSalesOwners] if owners else "default.owner@example.com"
    associatedCompanyDomain = random.choice(companyDomains) if companyDomains and random.random() < 0.7 else None
    contactEmail = fake.unique.email()
    try:
        contactPhone = fake.unique.phone_number()
    except Exception:
        contactPhone = fake.phone_number() + f"-{i}"
    try:
        contactMobilePhone = fake.unique.phone_number()
    except Exception:
        contactMobilePhone = fake.phone_number() + f"-{i+numContacts}"
    contact = {
        'Contact ID': contactId,
        'First Name': firstName,
        'Last Name': lastName,
        'Email': contactEmail,
        'Phone Number': contactPhone,
        'Mobile Phone Number': contactMobilePhone,
        'Job Title': fake.job(),
        'Lifecycle Stage': lifecycleStage,
        'Lead Status': leadStatus,
        'Create Date': createDate.isoformat(),
        'Last Modified Date': lastModifiedDate.isoformat(),
        'Contact Owner': contactOwner,
        'Lead Source': random.choice(['Organic Search', 'Paid Search', 'Social Media', 'Referral', 'Offline Sources', 'Direct Traffic', 'Email Marketing', 'Other Campaigns']),
        'Website URL': fake.url() if random.random() < 0.3 else None,
        'Street Address': fake.street_address(),
        'City': fake.city(),
        'State/Region': fake.state_abbr(),
        'Postal Code': fake.zipcode(),
        'Country': fake.country(),
        'Associated Company Domain': associatedCompanyDomain
    }
    contactsData.append(contact)
fake.unique.clear()

print("Generating Deals...")
dealFieldnames = [
    'Deal ID', 'Deal Name', 'Deal Stage', 'Pipeline', 'Amount',
    'Close Date', 'Create Date', 'Deal Owner', 'Deal Type',
    'Closed Lost Reason',
    'Associated Company Domain',
    'Associated Contact Email'
]
contactsForDeals = [
    (c['Email'], c['Associated Company Domain'])
    for c in contactsData if c.get('Associated Company Domain')
]
if contactsForDeals:
    for i in range(numDeals):
        dealId = f"DEAL-{uuid.uuid4()}"
        createDate = generateRandomDate(startDate=datetime.date(2023, 1, 1))
        dealStage = random.choice(dealStages)
        dealOwner = owners[i % numSalesOwners] if owners else "default.owner@example.com"
        if dealStage in ['Closed Won', 'Closed Lost']:
            closeDate = generateRandomDate(startDate=createDate)
        else:
            closeDate = generateRandomDate(startDate=datetime.date.today(), endDate=datetime.date.today() + datetime.timedelta(days=180))
        closedLostReason = random.choice(closedLostReasons) if dealStage == 'Closed Lost' else None
        associatedContactEmail, associatedCompanyDomain = random.choice(contactsForDeals)
        companyName = next((c['Company Name'] for c in companiesData if c.get('Company Domain Name') == associatedCompanyDomain), "Unknown Company")
        dealName = f"{companyName} - {random.choice(dealTypes)} Opportunity"
        deal = {
            'Deal ID': dealId,
            'Deal Name': dealName,
            'Deal Stage': dealStage,
            'Pipeline': random.choice(dealPipelines),
            'Amount': round(random.uniform(1000, 250000), 2),
            'Close Date': closeDate.isoformat(),
            'Create Date': createDate.isoformat(),
            'Deal Owner': dealOwner,
            'Deal Type': random.choice(dealTypes),
            'Closed Lost Reason': closedLostReason,
            'Associated Company Domain': associatedCompanyDomain,
            'Associated Contact Email': associatedContactEmail
        }
        dealsData.append(deal)

print("Generating Tickets...")
ticketFieldnames = [
    'Ticket ID', 'Ticket Name', 'Ticket Description', 'Ticket Status',
    'Pipeline', 'Ticket Priority', 'Create Date', 'Last Activity Date',
    'Close Date', 'Ticket Owner', 'Ticket Source',
    'Associated Company Domain',
    'Associated Contact Email'
]
contactsForTickets = [
    (c['Email'], c.get('Associated Company Domain'))
    for c in contactsData
]
numSupportOwners = len(supportOwners) if supportOwners else 1
if contactsForTickets:
    for i in range(numTickets):
        ticketId = f"TICK-{uuid.uuid4()}"
        createDate = generateRandomDate(startDate=datetime.date(2023, 6, 1))
        lastActivityDate = generateRandomDate(startDate=createDate)
        ticketStatus = random.choice(ticketStatuses)
        closeDate = generateRandomDate(startDate=lastActivityDate) if ticketStatus == 'Closed' else None
        ticketOwner = supportOwners[i % numSupportOwners] if supportOwners else "default.support@example.com"
        associatedContactEmail, associatedCompanyDomain = random.choice(contactsForTickets)
        ticket = {
            'Ticket ID': ticketId,
            'Ticket Name': fake.bs().capitalize(),
            'Ticket Description': fake.paragraph(nb_sentences=3),
            'Ticket Status': ticketStatus,
            'Pipeline': random.choice(ticketPipelines),
            'Ticket Priority': random.choice(ticketPriorities),
            'Create Date': createDate.isoformat(),
            'Last Activity Date': lastActivityDate.isoformat(),
            'Close Date': closeDate.isoformat() if closeDate else None,
            'Ticket Owner': ticketOwner,
            'Ticket Source': random.choice(ticketSources),
            'Associated Company Domain': associatedCompanyDomain,
            'Associated Contact Email': associatedContactEmail
        }
        ticketsData.append(ticket)

print("Generating Activities...")
activityFieldnames = [
    'Activity ID', 'Activity Type', 'Activity Date', 'Activity Owner',
    'Notes/Description', 'Call/Meeting Title/Subject', 'Call Outcome',
    'Meeting Outcome', 'Task Status', 'Task Due Date',
    'Associated Contact Email'
]
allContactEmails = [c['Email'] for c in contactsData if c.get('Email')]
if allContactEmails:
    for i in range(numActivities):
        activityId = f"ACT-{uuid.uuid4()}"
        activityType = random.choice(activityTypes)
        activityDate = generateRandomDate()
        owner = random.choice(allOwners) if allOwners else "default.activity@example.com"
        assocContactEmail = random.choice(allContactEmails)
        title = None
        callOutcome = None
        meetingOutcome = None
        taskStatus = None
        taskDueDate = None
        if activityType == 'Call':
            title = f"Call with contact {assocContactEmail}"
            callOutcome = random.choice(callOutcomes)
        elif activityType == 'Meeting':
            title = f"Meeting regarding contact {assocContactEmail}"
            meetingOutcome = random.choice(meetingOutcomes)
        elif activityType == 'Task':
            title = f"Follow up task for contact {assocContactEmail}"
            taskStatus = random.choice(taskStatuses)
            if taskStatus != 'Completed':
                taskDueDate = generateRandomDate(startDate=datetime.date.today(), endDate=datetime.date.today() + datetime.timedelta(days=30))
        activity = {
            'Activity ID': activityId,
            'Activity Type': activityType,
            'Activity Date': activityDate.isoformat(),
            'Activity Owner': owner,
            'Notes/Description': fake.paragraph(nb_sentences=2) if activityType in ['Note', 'Email'] else fake.sentence(),
            'Call/Meeting Title/Subject': title,
            'Call Outcome': callOutcome,
            'Meeting Outcome': meetingOutcome,
            'Task Status': taskStatus,
            'Task Due Date': taskDueDate.isoformat() if taskDueDate else None,
            'Associated Contact Email': assocContactEmail
        }
        activitiesData.append(activity)

print("Writing data to CSV files...")
if companiesData:
    writeToCsv(companiesData, 'hubspot_companies.csv', companyFieldnames)
if contactsData:
    writeToCsv(contactsData, 'hubspot_contacts.csv', contactFieldnames)
if dealsData:
    writeToCsv(dealsData, 'hubspot_deals.csv', dealFieldnames)
if ticketsData:
    writeToCsv(ticketsData, 'hubspot_tickets.csv', ticketFieldnames)
if activitiesData:
    writeToCsv(activitiesData, 'hubspot_activities.csv', activityFieldnames)

print("--- Data Generation Complete ---")
print(f"Generated {len(companiesData)} companies.")
print(f"Generated {len(contactsData)} contacts.")
print(f"Generated {len(dealsData)} deals.")
print(f"Generated {len(ticketsData)} tickets.")
print(f"Generated {len(activitiesData)} activities.")
print("Import CSV files into HubSpot in this order:")
print("1. hubspot_companies.csv")
print("2. hubspot_contacts.csv")
print("3. hubspot_deals.csv")
print("4. hubspot_tickets.csv")
print("5. hubspot_activities.csv")
