from patent_client import USApplication

google_apps = USApplication.objects.filter(first_named_applicant='Google LLC')

res =  len(google_apps) > 1000

print(google_apps[0].patent_number)

print(res)

