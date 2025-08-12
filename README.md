# central-companion
A set of functions to use with the new version of HPE Aruba Networking Central


Now with complete CRUD examples.

## Get
get_sites.py - returns a list of sites.

## Post
create_sites.py - passes a dictionary to HTTP POST

## Delete
delete_site_by_name.py - Uses HTTP DELETE

## Put
put_site_by_name.py - Update any key/value pair in the site information. HTTP PUT.


### Simplified access

utility.get_client - returns the client (TOKEN)

utility.api_caller.py - Send client, api_method, api_path, and api_data
