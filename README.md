# TheSeedBox
## Dependencies
    cd TheSeedBox/api
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

To refresh the Python code after pulling changes, run `sudo restart seedbox`.

## Server configuration

nginx configuration: `sudo vim /etc/nginx/sites-available/seedbox`

uwsgi service configuration: `sudo vim /etc/init/seedbox.conf`


# API documentation

## Database

###OPERATOR List
==, eq, equals, equals_to

!=, neq, does_not_equal, not_equal_to

\>, gt, <, lt

\>=, ge, gte, geq, <=, le, lte, leq

in, not_in

is_null, is_not_null

like

has

any






###Get Entire Table
URL: https://website/api/TABLENAME

TYPE: GET

Parameters:

Return: JSON

Example: See Example 1



###Select
URL: https://website/api/TABLENAME

TYPE: GET

Parameters: JSON

{'q': '{"filters": [{"name": "COLUMN_NAME", "val": "COLUMN_VALUE", "op": "OPERATOR"}]}'}

Return: JSON

Example: See Example 1




###Delete
URL: https://website/api/TABLENAME/ID

TYPE: DELETE

Response: HTTP/1.1 204 No Content


###Update -> NOT implemented TODO
URL: https://website/api/TABLENAME/ID

Type: PUT

Parameters: JSON

{"COLUMN_NAME": "VALUE"}

Return: JSON

Example:

HTTP/1.1 200 OK

See Example 1


###Insert
URL: https://website/api/TABLENAME

Type: POST

Parameters: JSON

{"COLUMN_NAME": "VALUE"}

Return: JSON

Example:

HTTP/1.1 201 Created

See Example 1

###Example 1:
{
  "num_results": 1,
  "objects": [
    {
      "email": "test@website",
      "fname": "Test",
      "id": 1,
      "lname": "User",
      "password": "pass123"
    }
  ],
  "page": 1,
  "total_pages": 1
}


## Routes
