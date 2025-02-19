from patent_client import USPublishedApplication
from datetime import datetime

def get_published_applications(publication_date):
    """
    Retrieve patent applications published on a specific date.
    
    Args:
        publication_date (str): Date in format 'YYYY-MM-DD'
    
    Returns:
        list: List of published patent applications
    """
    # Query applications published on the specified date
    query = USPublishedApplication.objects.filter(
        publication_date=publication_date
    )
    
    # Create a list to store application information
    applications = []
    
    # Iterate through the results and store relevant information
    for app in query:
        app_info = {
            'application_number': app.application_number,
            'patent_title': app.patent_title,
            'inventors': app.inventors,
            'publication_date': app.publication_date
        }
        applications.append(app_info)
    
    return applications

def main():
    # Example usage with a specific date
    publication_date = "2025-02-13"  # Format: YYYY-MM-DD
    
    print(f"Fetching patent applications published on {publication_date}")
    applications = get_published_applications(publication_date)
    
    # Print the results
    print(f"\nFound {len(applications)} applications:")
    for i, app in enumerate(applications, 1):
        print(f"\n{i}. Application Number: {app['application_number']}")
        print(f"   Title: {app['patent_title']}")
        print(f"   Inventors: {', '.join(app['inventors']) if app['inventors'] else 'Not specified'}")
        print(f"   Publication Date: {app['publication_date']}")

if __name__ == "__main__":
    main()
