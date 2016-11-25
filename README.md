# TheSeedBox

Table of Contents
=================

  * [TheSeedBox](#theseedbox)
    * [Dependencies](#dependencies)
    * [Server configuration](#server-configuration)
  * [API documentation](#api-documentation)
    * [Database](#database)
      * [OPERATOR List](#operator-list)
      * [Get Entire Table](#get-entire-table)
      * [Select](#select)
      * [Delete](#delete)
      * [Update](#update)
      * [Insert](#insert)
      * [Example 1:](#example-1)
    * [Extra Routes](#extra-routes)
      * [Upload](#upload)
      * [Download](#download)
      * [List Tables](#list-tables)
      * [List Files](#list-files)
      * [Authenticate](#authenticate)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

## Dependencies

```bash
cd TheSeedBox/api
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To refresh the Python code after pulling changes, run `sudo restart seedbox`

## Server configuration

nginx configuration: `sudo vim /etc/nginx/sites-available/seedbox`

uwsgi service configuration: `sudo vim /etc/init/seedbox.conf`


# API documentation

## Database

### OPERATOR List

```SQL
==, eq, equals, equals_to

!=, neq, does_not_equal, not_equal_to

\>, gt, <, lt

\>=, ge, gte, geq, <=, le, lte, leq

in, not_in

is_null, is_not_null

like

has

any
```

### Get Entire Table

URL: `/api/TABLENAME`

TYPE: `GET`

Parameters: ``

Return: `JSON`

> Example: See Example 1

### Select
URL: `/api/TABLENAME`

TYPE: `GET`

Parameters: `JSON`

```JavaScript
{'q': '{"filters": [{"name": "COLUMN_NAME", "val": "COLUMN_VALUE", "op": "OPERATOR"}]}'}
```

Return: `JSON`

> Example: See Example 1

### Delete
URL: `/api/TABLENAME/ID`

TYPE: `DELETE`

Return: `HTTP/1.1 204 No Content`

###Update

URL: `/api/TABLENAME/ID`

Type: `PUT`

Parameters: `JSON`

{"COLUMN_NAME": "VALUE"}

Return: `JSON`

Example:

> HTTP/1.1 200 OK

> See Example 1

### Insert

URL: `/api/TABLENAME`

Type: `POST`

Parameters: `JSON`

{"COLUMN_NAME": "VALUE"}

Return: `JSON`

Example:

> HTTP/1.1 201 Created

> See Example 1

###Example 1:

```JavaScript
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
```

## Extra Routes

### Upload

URL: `/api/upload`

Type: `POST`

Parameters: `file`

Return: `JSON`

"Success"

###Download
URL: `/api/download/FILENAME`

Type: `GET`

Return: `File`

###List Tables
URL: `/api/tables`

Type: `GET`

Return: `JSON`

```JavaScript
{
  "tablenames": [
    "ScraperSettings",
    "Users",
    "PodOrderForms",
    "Scraper",
    "GardenFreshBoxes",
    "Produce",
    "Products",
    "GFB",
    "Retailers",
    "Test"
  ]
}
```

### List Files
URL: `/api/files`

Type: `GET`

Return: `JSON`

```JavaScript
{
  "files": [
    "a.csv",
    "Supplier_Price_List_WE_September_23-2016.csv",
    "test.csv",
    "CIS3750_A2_Requirements_Screaming_Programmers.csv"
  ]
}
```

### Authenticate

URL: `/api/authenticate`

Type `POST`

Parameters: `email, password`

Return: `JSON` => `{"success=true"}` or `{"Authentication error"}`

### Run scraper manually

URL: `/api/run_scraper`

Type `POST`

Parameters: `nofrills, metro`

Return: `JSON` => `{"success=true"}` or `{"Error"}`
