# HubSpot Dummy Data Generator

This Python script generates realistic dummy data for various HubSpot objects (Companies, Contacts, Deals, Tickets, Activities) and saves them into separate CSV files. These files can then be imported into HubSpot to populate a sandbox or testing environment.

## Features

* Generates data for:
    * Companies
    * Contacts
    * Deals
    * Tickets
    * Activities
* Uses the `Faker` library to create realistic-looking names, emails, addresses, etc.
* Uses UUIDs for potentially more robust unique IDs.
* Configurable number of records for each object type (see Configuration section).
* Configurable lists for custom fields like industry, deal stage, ticket status, etc.
* Attempts to create logical associations between records (e.g., contacts associated with companies, deals/tickets associated with contacts and companies).
* Outputs data into separate CSV files ready for HubSpot import.

## Dependencies

This script requires the following Python library:

* `Faker`: Used for generating fake data.

You can install it using pip:
```bash
pip install Faker
```

Configuration and Customization

You can customize the data generation process by modifying the variables in the `# --- Configuration ---` section at the top of the `huspotDummyData.py` script:

* **Record Counts:**

  * `NUM_COMPANIES`: Number of company records (default: 200).

  * `NUM_CONTACTS`: Number of contact records (default: 950). *See Limitations section regarding this number.*

  * `NUM_DEALS`: Number of deal records (default: 500).

  * `NUM_TICKETS`: Number of ticket records (default: 300).

  * `NUM_ACTIVITIES`: Number of activity records (default: 2000).

  * **How to Change:** Simply change the integer value assigned to these variables (e.g., `NUM_CONTACTS = 2000`). Be mindful of potential performance impacts or limitations when generating very large numbers of records (see Limitations section below).

* **Field Values:**

  * `LIFECYCLE_STAGES`, `LEAD_STATUSES`, `INDUSTRIES`, `DEAL_STAGES`, `TICKET_PRIORITIES`, etc.: These lists define the possible values randomly assigned to corresponding HubSpot fields.

  * **How to Change:** Modify the Python lists by adding, removing, or changing the string values within them to match your specific HubSpot setup or testing needs. Remember that `None` is included in some lists (like `LEAD_STATUSES`) to allow for blank values.

* **Record Owners:**

  * `OWNERS`, `SUPPORT_OWNERS`: Define the pool of user email addresses assigned to records. Sales owners (`OWNERS`) are assigned to companies, contacts, and deals. Support owners (`SUPPORT_OWNERS`) are assigned to tickets. All owners (`ALL_OWNERS`) can be assigned to activities.

  * **How to Change:** Update the lists with the actual or desired fake email addresses. The script cycles through these lists for assignment.

## How to Run

1. Ensure you have Python and the `Faker` library installed.

2. Save the script as `huspotDummyData.py`.

3. Open a terminal or command prompt.

4. Navigate to the directory where you saved the script.

5. Run the script using:  ```python huspotDummyData.py```

6. The script will print progress messages to the console and generate the CSV files in the same directory.

## Output Files

The script generates the following CSV files:

* `hubspot_companies.csv`: Contains company data.

* `hubspot_contacts.csv`: Contains contact data.

* `hubspot_deals.csv`: Contains deal data.

* `hubspot_tickets.csv`: Contains ticket data.

* `hubspot_activities.csv`: Contains activity data (simplified for CSV import, primarily associated with contacts via email).

## HubSpot Import Instructions

Import the generated CSV files into your HubSpot portal in the following order to ensure associations are created correctly:

1. **`hubspot_companies.csv`**:

* Object Type: Companies

* Mapping: **Use 'Company Domain Name' as the unique identifier**.

2. **`hubspot_contacts.csv`**:

* Object Type: Contacts

* Mapping: **Use** 'Email' as the **unique identifier**. Use 'Associated Company Domain' to link to companies.

3. **`hubspot_deals.csv`**:

* Object Type: Deals

* Mapping: Use 'Associated Contact Email' and 'Associated Company Domain' to link deals to contacts and companies.

4. **`hubspot_tickets.csv`**:

* Object Type: Tickets

* Mapping: Use 'Associated Contact Email' and 'Associated Company Domain' to link tickets to contacts and companies.

5. **`hubspot_activities.csv`**:

* Object Type: Activities

* Mapping: **Use 'Associated Contact Email' to link the activity to the contact**.

**Important:** Always carefully review
