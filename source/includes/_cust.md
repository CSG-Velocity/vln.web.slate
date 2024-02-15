

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="slp-service1-0">SLP Service1.0 v1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

API Description

<a href="https://velocitymsp.ai">Terms of service</a>
Email: <a href="mailto:support@velocitymsp.ai">Support</a> 
License: <a href="https://velocitymsp.ai/license1">Example License</a>

# Authentication

* API Key (Bearer)
    - Parameter Name: **Authorization**, in: header. JWT Authorization header {token}

<h1 id="slp-service1-0-client">Client</h1>

## post__api_v1_Client_AddBusinessWorkLocation

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Client/AddBusinessWorkLocation \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Client/AddBusinessWorkLocation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "customerWorkLocationId": 0,
  "refId": 0,
  "refType": "string",
  "workLocation": "string",
  "latitude": 0.1,
  "longitude": 0.1,
  "address": "string",
  "zip": "string",
  "countryId": 0,
  "stateId": 0,
  "cityId": 0,
  "phoneCode": 0,
  "phone": "string",
  "fax": "string",
  "legalEntityName": "string",
  "title": "string",
  "website": "string",
  "notes": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "billingFirstName": "string",
  "billingLastName": "string",
  "billingAddress": "string",
  "billingCityId": 0,
  "billingStateId": 0,
  "billingZip": "string",
  "billingCountryId": 0,
  "shippingFirstName": "string",
  "shippingLastName": "string",
  "shippingAddress": "string",
  "shippingCityId": 0,
  "shippingStateId": 0,
  "shippingZip": "string",
  "shippingCountryId": 0,
  "role": "string",
  "loginId": 0,
  "unitNumber": "string",
  "clockInRadius": 0,
  "mainPhoneCountryCode": 0,
  "mainPhone": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Client/AddBusinessWorkLocation',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Client/AddBusinessWorkLocation',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Client/AddBusinessWorkLocation', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Client/AddBusinessWorkLocation', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Client/AddBusinessWorkLocation");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Client/AddBusinessWorkLocation", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Client/AddBusinessWorkLocation`

> Body parameter

```json
{
  "customerWorkLocationId": 0,
  "refId": 0,
  "refType": "string",
  "workLocation": "string",
  "latitude": 0.1,
  "longitude": 0.1,
  "address": "string",
  "zip": "string",
  "countryId": 0,
  "stateId": 0,
  "cityId": 0,
  "phoneCode": 0,
  "phone": "string",
  "fax": "string",
  "legalEntityName": "string",
  "title": "string",
  "website": "string",
  "notes": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "billingFirstName": "string",
  "billingLastName": "string",
  "billingAddress": "string",
  "billingCityId": 0,
  "billingStateId": 0,
  "billingZip": "string",
  "billingCountryId": 0,
  "shippingFirstName": "string",
  "shippingLastName": "string",
  "shippingAddress": "string",
  "shippingCityId": 0,
  "shippingStateId": 0,
  "shippingZip": "string",
  "shippingCountryId": 0,
  "role": "string",
  "loginId": 0,
  "unitNumber": "string",
  "clockInRadius": 0,
  "mainPhoneCountryCode": 0,
  "mainPhone": "string"
}
```

<h3 id="post__api_v1_client_addbusinessworklocation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.AddBusinessWorkLocationModelRequest](#schemaslp.services.domain.model.request.addbusinessworklocationmodelrequest)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_client_addbusinessworklocation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|417|[Expectation Failed](https://tools.ietf.org/html/rfc7231#section-6.5.14)|Client Error|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Client_FetchWorkLocations

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Client/FetchWorkLocations \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Client/FetchWorkLocations HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "customerId": 0,
  "searchKey": "string",
  "pageNumber": 0,
  "pageSize": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Client/FetchWorkLocations',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Client/FetchWorkLocations',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Client/FetchWorkLocations', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Client/FetchWorkLocations', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Client/FetchWorkLocations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Client/FetchWorkLocations", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Client/FetchWorkLocations`

> Body parameter

```json
{
  "customerId": 0,
  "searchKey": "string",
  "pageNumber": 0,
  "pageSize": 0
}
```

<h3 id="post__api_v1_client_fetchworklocations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.Client.FetchWorkLocationsRequestModel](#schemaslp.services.domain.model.request.client.fetchworklocationsrequestmodel)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_client_fetchworklocations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Client_AssignContactToWorkLocation

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Client/AssignContactToWorkLocation \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Client/AssignContactToWorkLocation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "customerContactId": 0,
  "customerWorkLocationId": 0,
  "isDeleted": true,
  "workLocationRoleId": 0,
  "loginId": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Client/AssignContactToWorkLocation',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Client/AssignContactToWorkLocation',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Client/AssignContactToWorkLocation', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Client/AssignContactToWorkLocation', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Client/AssignContactToWorkLocation");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Client/AssignContactToWorkLocation", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Client/AssignContactToWorkLocation`

> Body parameter

```json
{
  "customerContactId": 0,
  "customerWorkLocationId": 0,
  "isDeleted": true,
  "workLocationRoleId": 0,
  "loginId": 0
}
```

<h3 id="post__api_v1_client_assigncontacttoworklocation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.Client.AssignContactToWorkLocationRequestModel](#schemaslp.services.domain.model.request.client.assigncontacttoworklocationrequestmodel)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_client_assigncontacttoworklocation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Client_GetClientWorkLocations

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Client/GetClientWorkLocations \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Client/GetClientWorkLocations HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "intStart": 0,
  "customerID": "string",
  "workLocationSearch": "string",
  "workLocationStatus": 0,
  "intPageSize": 0,
  "intSortColumn": 0,
  "sortDirection": "string",
  "address": "string",
  "contactPerson": "string",
  "contactDetails": "string",
  "isExport": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Client/GetClientWorkLocations',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Client/GetClientWorkLocations',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Client/GetClientWorkLocations', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Client/GetClientWorkLocations', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Client/GetClientWorkLocations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Client/GetClientWorkLocations", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Client/GetClientWorkLocations`

> Body parameter

```json
{
  "intStart": 0,
  "customerID": "string",
  "workLocationSearch": "string",
  "workLocationStatus": 0,
  "intPageSize": 0,
  "intSortColumn": 0,
  "sortDirection": "string",
  "address": "string",
  "contactPerson": "string",
  "contactDetails": "string",
  "isExport": 0
}
```

<h3 id="post__api_v1_client_getclientworklocations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.Client.ClientWorkLocationRequestModel](#schemaslp.services.domain.model.request.client.clientworklocationrequestmodel)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_client_getclientworklocations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Client_GetCustomerWLContacts

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Client/GetCustomerWLContacts \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Client/GetCustomerWLContacts HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "intStart": 0,
  "intPageSize": 0,
  "intSortColumn": 0,
  "sortDirection": "string",
  "customerWorkLocationId": 0,
  "customerContactId": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Client/GetCustomerWLContacts',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Client/GetCustomerWLContacts',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Client/GetCustomerWLContacts', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Client/GetCustomerWLContacts', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Client/GetCustomerWLContacts");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Client/GetCustomerWLContacts", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Client/GetCustomerWLContacts`

> Body parameter

```json
{
  "intStart": 0,
  "intPageSize": 0,
  "intSortColumn": 0,
  "sortDirection": "string",
  "customerWorkLocationId": 0,
  "customerContactId": 0
}
```

<h3 id="post__api_v1_client_getcustomerwlcontacts-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.Client.GetCustomerWLContactsRequestModel](#schemaslp.services.domain.model.request.client.getcustomerwlcontactsrequestmodel)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_client_getcustomerwlcontacts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get__api_v1_Client_GetCustomerWorkLocationContactList

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/Client/GetCustomerWorkLocationContactList \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/v1/Client/GetCustomerWorkLocationContactList HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Client/GetCustomerWorkLocationContactList',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/v1/Client/GetCustomerWorkLocationContactList',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/v1/Client/GetCustomerWorkLocationContactList', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/Client/GetCustomerWorkLocationContactList', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Client/GetCustomerWorkLocationContactList");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/Client/GetCustomerWorkLocationContactList", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/Client/GetCustomerWorkLocationContactList`

<h3 id="get__api_v1_client_getcustomerworklocationcontactlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|CustId|query|string|false|none|
|WorkLocationId|query|integer(int32)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="get__api_v1_client_getcustomerworklocationcontactlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Client_DeleteCustomerWorkLocationContact

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Client/DeleteCustomerWorkLocationContact \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Client/DeleteCustomerWorkLocationContact HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "custWorkLocation_ContactId": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Client/DeleteCustomerWorkLocationContact',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Client/DeleteCustomerWorkLocationContact',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Client/DeleteCustomerWorkLocationContact', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Client/DeleteCustomerWorkLocationContact', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Client/DeleteCustomerWorkLocationContact");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Client/DeleteCustomerWorkLocationContact", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Client/DeleteCustomerWorkLocationContact`

> Body parameter

```json
{
  "custWorkLocation_ContactId": 0
}
```

<h3 id="post__api_v1_client_deletecustomerworklocationcontact-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|WorkLocationId|query|integer(int32)|false|none|
|body|body|[SLP.Services.Domain.Model.Request.Client.DeleteCustomerWorkLocationContactRequestModel](#schemaslp.services.domain.model.request.client.deletecustomerworklocationcontactrequestmodel)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_client_deletecustomerworklocationcontact-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|417|[Expectation Failed](https://tools.ietf.org/html/rfc7231#section-6.5.14)|Client Error|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="slp-service1-0-job">Job</h1>

## get__api_v1_Job_TestVersioning

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/Job/TestVersioning \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/v1/Job/TestVersioning HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Job/TestVersioning',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/v1/Job/TestVersioning',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/v1/Job/TestVersioning', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/Job/TestVersioning', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Job/TestVersioning");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/Job/TestVersioning", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/Job/TestVersioning`

> Example responses

> 200 Response

```json
{
  "id": 0,
  "job_title": "string",
  "job_details": "string",
  "requisition_id": "string",
  "status": "string",
  "created_at": "string",
  "opened_at": "string",
  "closed_at": "string",
  "updated_at": "string",
  "number_of_openings": 0,
  "notes": "string",
  "start_at": "string",
  "end_at": "string",
  "shift_start_time": "string",
  "shift_end_time": "string",
  "departments": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "offices": [
    null
  ],
  "employment_type": {
    "id": "string",
    "name": "string"
  },
  "budget": {
    "bill_rate": "string",
    "currency": "string",
    "unit": "string"
  },
  "hiring_team": {
    "hiring_managers": [
      {
        "id": 0,
        "first_Name": "string",
        "last_Name": "string",
        "name": "string"
      }
    ],
    "recruiters": [
      {
        "id": 0,
        "first_Name": "string",
        "last_Name": "string",
        "name": "string"
      }
    ]
  }
}
```

<h3 id="get__api_v1_job_testversioning-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[SLP.Services.Domain.Model.Response.JobByIdResponse](#schemaslp.services.domain.model.response.jobbyidresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get__api_v1_Job_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/Job/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/v1/Job/{id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Job/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/v1/Job/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/v1/Job/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/Job/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Job/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/Job/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/Job/{id}`

*Retrieve details by Id*

<h3 id="get__api_v1_job_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int64)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "job_title": "string",
  "job_details": "string",
  "requisition_id": "string",
  "status": "string",
  "created_at": "string",
  "opened_at": "string",
  "closed_at": "string",
  "updated_at": "string",
  "number_of_openings": 0,
  "notes": "string",
  "start_at": "string",
  "end_at": "string",
  "shift_start_time": "string",
  "shift_end_time": "string",
  "departments": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "offices": [
    null
  ],
  "employment_type": {
    "id": "string",
    "name": "string"
  },
  "budget": {
    "bill_rate": "string",
    "currency": "string",
    "unit": "string"
  },
  "hiring_team": {
    "hiring_managers": [
      {
        "id": 0,
        "first_Name": "string",
        "last_Name": "string",
        "name": "string"
      }
    ],
    "recruiters": [
      {
        "id": 0,
        "first_Name": "string",
        "last_Name": "string",
        "name": "string"
      }
    ]
  }
}
```

<h3 id="get__api_v1_job_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[SLP.Services.Domain.Model.Response.JobByIdResponse](#schemaslp.services.domain.model.response.jobbyidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Job

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Job \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Job HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "id": 0,
  "templatE_JOB_ID": 0,
  "number_of_openings": 1,
  "jobTitle": "string",
  "department_id": 0,
  "offices": {
    "id": 0,
    "location": {
      "city_name": "string",
      "state_id": 0,
      "country_id": 0
    }
  },
  "requisition_id": "string",
  "start_at": "2019-08-24T14:15:22Z",
  "end_at": "2019-08-24T14:15:22Z",
  "shift_start_time": "string",
  "shift_end_time": "string",
  "notes": "string",
  "status": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "opened_at": "2019-08-24T14:15:22Z",
  "closed_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z",
  "employment_type": "string",
  "budget": {
    "bill_rate": 0.1,
    "currency": "string",
    "unit": 0
  },
  "hiring_managers_id": 0,
  "job_details": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Job',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Job',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Job', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Job', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Job");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Job", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Job`

*Create a new Job*

> Body parameter

```json
{
  "id": 0,
  "templatE_JOB_ID": 0,
  "number_of_openings": 1,
  "jobTitle": "string",
  "department_id": 0,
  "offices": {
    "id": 0,
    "location": {
      "city_name": "string",
      "state_id": 0,
      "country_id": 0
    }
  },
  "requisition_id": "string",
  "start_at": "2019-08-24T14:15:22Z",
  "end_at": "2019-08-24T14:15:22Z",
  "shift_start_time": "string",
  "shift_end_time": "string",
  "notes": "string",
  "status": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "opened_at": "2019-08-24T14:15:22Z",
  "closed_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z",
  "employment_type": "string",
  "budget": {
    "bill_rate": 0.1,
    "currency": "string",
    "unit": 0
  },
  "hiring_managers_id": 0,
  "job_details": "string"
}
```

<h3 id="post__api_v1_job-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.CreateJobRequestModel](#schemaslp.services.domain.model.request.createjobrequestmodel)|false|none|

> Example responses

> 200 Response

```json
true
```

<h3 id="post__api_v1_job-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|boolean|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get__api_v1_Job

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/Job \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/v1/Job HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Job',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/v1/Job',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/v1/Job', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/Job', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Job");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/Job", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/Job`

*List of jobs based on filter criteria*

<h3 id="get__api_v1_job-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|IntStart|query|integer(int32)|false|none|
|IntPageSize|query|integer(int32)|false|none|
|IntSortColumn|query|integer(int32)|false|none|
|SortDirection|query|string|false|none|
|Created_before|query|string|false|none|
|Created_after|query|string|false|none|
|Updated_before|query|string|false|none|
|Updated_after|query|string|false|none|
|Status|query|string|false|none|
|DepartmentId|query|integer(int32)|false|none|
|OfficeId|query|integer(int32)|false|none|

> Example responses

> 200 Response

```json
{
  "cjM_JOB_ID": 0,
  "cjM_JOB_TITLE": "string",
  "customerWorkLocationId": 0,
  "workLocation": "string",
  "latitude": 0.1,
  "longitude": 0.1,
  "customerContactId": 0,
  "firstName": "string",
  "lastName": "string",
  "customerDepartment_Id": 0,
  "departmentName": "string",
  "jlp_Skill_Id": 0,
  "skillName": "string",
  "nuM_OF_POSITIONS": 0,
  "billRate": 0.1,
  "oTrate": 0.1,
  "holidayRate": 0.1,
  "clockInRadius": 0,
  "cityName": "string",
  "stateName": "string",
  "zip": "string",
  "address": "string",
  "cjM_JOB_DETAILS": "string",
  "uniformDescription": "string",
  "projectStartDate": "2019-08-24T14:15:22Z",
  "projectEndDate": "2019-08-24T14:15:22Z",
  "shiftTimingFrom": "string",
  "shiftTimingTo": "string",
  "specialInstructions": "string",
  "jobShiftDetails": [
    {
      "jobShiftDetailId": 0,
      "date": "2019-08-24T14:15:22Z",
      "startTime": "string",
      "endTime": "string",
      "isDeleted": true
    }
  ],
  "reportToLocation": "string"
}
```

<h3 id="get__api_v1_job-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[SLP.Services.Domain.Model.JobDetailsResponse](#schemaslp.services.domain.model.jobdetailsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## patch__api_v1_Job_id

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/v1/Job/id \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
PATCH /api/v1/Job/id HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "id": 0,
  "template_job_id": 0,
  "number_of_openings": 1,
  "jobTitle": "string",
  "department_id": 0,
  "offices": {
    "id": 0,
    "location": {
      "city_name": "string",
      "state_id": 0,
      "country_id": 0
    }
  },
  "requisition_id": "string",
  "start_at": "2019-08-24T14:15:22Z",
  "end_at": "2019-08-24T14:15:22Z",
  "shift_start_time": "string",
  "shift_end_time": "string",
  "notes": "string",
  "status": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "opened_at": "2019-08-24T14:15:22Z",
  "closed_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z",
  "employment_type": "string",
  "budget": {
    "bill_rate": 0.1,
    "currency": "string",
    "unit": 0
  },
  "hiring_managers_id": 0,
  "job_details": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Job/id',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.patch '/api/v1/Job/id',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.patch('/api/v1/Job/id', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/v1/Job/id', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Job/id");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/v1/Job/id", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/v1/Job/id`

*Update an existing Job*

> Body parameter

```json
{
  "id": 0,
  "template_job_id": 0,
  "number_of_openings": 1,
  "jobTitle": "string",
  "department_id": 0,
  "offices": {
    "id": 0,
    "location": {
      "city_name": "string",
      "state_id": 0,
      "country_id": 0
    }
  },
  "requisition_id": "string",
  "start_at": "2019-08-24T14:15:22Z",
  "end_at": "2019-08-24T14:15:22Z",
  "shift_start_time": "string",
  "shift_end_time": "string",
  "notes": "string",
  "status": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "opened_at": "2019-08-24T14:15:22Z",
  "closed_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z",
  "employment_type": "string",
  "budget": {
    "bill_rate": 0.1,
    "currency": "string",
    "unit": 0
  },
  "hiring_managers_id": 0,
  "job_details": "string"
}
```

<h3 id="patch__api_v1_job_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|query|integer(int64)|false|none|
|body|body|[SLP.Services.Domain.Model.Request.UpdateJobRequestModel](#schemaslp.services.domain.model.request.updatejobrequestmodel)|false|none|

> Example responses

> 200 Response

```json
true
```

<h3 id="patch__api_v1_job_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|boolean|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="slp-service1-0-login">Login</h1>

## post__api_v1_Login

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Login \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Login HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "email_Id": "user@example.com",
  "password": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Login',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Login',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Login', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Login', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Login");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Login", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Login`

*User authentication*

> Body parameter

```json
{
  "email_Id": "user@example.com",
  "password": "string"
}
```

<h3 id="post__api_v1_login-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.LoginRequestModel](#schemaslp.services.domain.model.request.loginrequestmodel)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_login-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Login_RefreshToken

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Login/RefreshToken \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Login/RefreshToken HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "accessToken": "string",
  "refreshToken": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Login/RefreshToken',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Login/RefreshToken',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Login/RefreshToken', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Login/RefreshToken', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Login/RefreshToken");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Login/RefreshToken", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Login/RefreshToken`

*Refreshes the token.*

> Body parameter

```json
{
  "accessToken": "string",
  "refreshToken": "string"
}
```

<h3 id="post__api_v1_login_refreshtoken-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.RefreshTokenRequest](#schemaslp.services.domain.model.request.refreshtokenrequest)|false|The refresh request.|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_login_refreshtoken-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Login_Logout

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Login/Logout \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Login/Logout HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Login/Logout',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Login/Logout',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Login/Logout', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Login/Logout', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Login/Logout");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Login/Logout", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Login/Logout`

*Logouts this instance.*

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_login_logout-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|417|[Expectation Failed](https://tools.ietf.org/html/rfc7231#section-6.5.14)|Client Error|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get__api_v1_Login_EmailValidation

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/Login/EmailValidation?EmailId=user%40example.com \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/v1/Login/EmailValidation?EmailId=user%40example.com HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Login/EmailValidation?EmailId=user%40example.com',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/v1/Login/EmailValidation',
  params: {
  'EmailId' => 'string(email)'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/v1/Login/EmailValidation', params={
  'EmailId': 'user@example.com'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/Login/EmailValidation', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Login/EmailValidation?EmailId=user%40example.com");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/Login/EmailValidation", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/Login/EmailValidation`

*User will enter email for login process*

<h3 id="get__api_v1_login_emailvalidation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|EmailId|query|string(email)|true|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="get__api_v1_login_emailvalidation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Login_ForgotPassword

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Login/ForgotPassword \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Login/ForgotPassword HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "emailAddress": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Login/ForgotPassword',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Login/ForgotPassword',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Login/ForgotPassword', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Login/ForgotPassword', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Login/ForgotPassword");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Login/ForgotPassword", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Login/ForgotPassword`

*Forgots the password.*

> Body parameter

```json
{
  "emailAddress": "string"
}
```

<h3 id="post__api_v1_login_forgotpassword-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.ForgotPasswordRequest](#schemaslp.services.domain.model.request.forgotpasswordrequest)|false|The request.|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_login_forgotpassword-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Login_IsForgetPasswordLinkValid

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Login/IsForgetPasswordLinkValid \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Login/IsForgetPasswordLinkValid HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "key": "string",
  "type": 1
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Login/IsForgetPasswordLinkValid',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Login/IsForgetPasswordLinkValid',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Login/IsForgetPasswordLinkValid', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Login/IsForgetPasswordLinkValid', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Login/IsForgetPasswordLinkValid");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Login/IsForgetPasswordLinkValid", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Login/IsForgetPasswordLinkValid`

*To Validate Forget password link*

> Body parameter

```json
{
  "key": "string",
  "type": 1
}
```

<h3 id="post__api_v1_login_isforgetpasswordlinkvalid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.LinkValidRequest](#schemaslp.services.domain.model.request.linkvalidrequest)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_login_isforgetpasswordlinkvalid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Login_ResetPassword

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Login/ResetPassword \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Login/ResetPassword HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "forgotPwdTokenKey": "string",
  "password": "string",
  "confirmPassword": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Login/ResetPassword',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Login/ResetPassword',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Login/ResetPassword', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Login/ResetPassword', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Login/ResetPassword");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Login/ResetPassword", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Login/ResetPassword`

> Body parameter

```json
{
  "forgotPwdTokenKey": "string",
  "password": "string",
  "confirmPassword": "string"
}
```

<h3 id="post__api_v1_login_resetpassword-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.ResetPasswordRequest](#schemaslp.services.domain.model.request.resetpasswordrequest)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_login_resetpassword-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="slp-service1-0-master">Master</h1>

## get__api_v1_Master_GetCountryList

> Code samples

```shell
# You can also use wget
curl -X GET /api/v1/Master/GetCountryList \
  -H 'Accept: text/plain' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/v1/Master/GetCountryList HTTP/1.1

Accept: text/plain

```

```javascript

const headers = {
  'Accept':'text/plain',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Master/GetCountryList',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'text/plain',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/v1/Master/GetCountryList',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'text/plain',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/v1/Master/GetCountryList', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'text/plain',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/v1/Master/GetCountryList', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Master/GetCountryList");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"text/plain"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/v1/Master/GetCountryList", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/v1/Master/GetCountryList`

<h3 id="get__api_v1_master_getcountrylist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|intCountryId|query|integer(int32)|false|none|
|strCountryCode|query|string|false|none|

> Example responses

> 400 Response

```
{"type":"string","title":"string","status":0,"detail":"string","instance":"string","property1":null,"property2":null}
```

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="get__api_v1_master_getcountrylist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Master_GetStatesListByCountryId

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Master/GetStatesListByCountryId \
  -H 'Content-Type: application/json' \
  -H 'Accept: text/plain' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Master/GetStatesListByCountryId HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

```javascript
const inputBody = '{
  "intCountry_Id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'text/plain',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Master/GetStatesListByCountryId',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'text/plain',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Master/GetStatesListByCountryId',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Master/GetStatesListByCountryId', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'text/plain',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Master/GetStatesListByCountryId', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Master/GetStatesListByCountryId");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"text/plain"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Master/GetStatesListByCountryId", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Master/GetStatesListByCountryId`

> Body parameter

```json
{
  "intCountry_Id": 0
}
```

<h3 id="post__api_v1_master_getstateslistbycountryid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.Master.GetStatesListRequestModel](#schemaslp.services.domain.model.request.master.getstateslistrequestmodel)|false|none|

> Example responses

> 400 Response

```
{"type":"string","title":"string","status":0,"detail":"string","instance":"string","property1":null,"property2":null}
```

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_master_getstateslistbycountryid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_v1_Master_GetCityListByStateId

> Code samples

```shell
# You can also use wget
curl -X POST /api/v1/Master/GetCityListByStateId \
  -H 'Content-Type: application/json' \
  -H 'Accept: text/plain' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/v1/Master/GetCityListByStateId HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

```javascript
const inputBody = '{
  "stateId": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'text/plain',
  'Authorization':'API_KEY'
};

fetch('/api/v1/Master/GetCityListByStateId',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'text/plain',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/v1/Master/GetCityListByStateId',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/v1/Master/GetCityListByStateId', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'text/plain',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/v1/Master/GetCityListByStateId', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/v1/Master/GetCityListByStateId");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"text/plain"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/v1/Master/GetCityListByStateId", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/v1/Master/GetCityListByStateId`

> Body parameter

```json
{
  "stateId": 0
}
```

<h3 id="post__api_v1_master_getcitylistbystateid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLP.Services.Domain.Model.Request.Master.GetCityListRequest](#schemaslp.services.domain.model.request.master.getcitylistrequest)|false|none|

> Example responses

> 400 Response

```
{"type":"string","title":"string","status":0,"detail":"string","instance":"string","property1":null,"property2":null}
```

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}
```

<h3 id="post__api_v1_master_getcitylistbystateid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

# Schemas

<h2 id="tocS_Microsoft.AspNetCore.Mvc.ProblemDetails">Microsoft.AspNetCore.Mvc.ProblemDetails</h2>
<!-- backwards compatibility -->
<a id="schemamicrosoft.aspnetcore.mvc.problemdetails"></a>
<a id="schema_Microsoft.AspNetCore.Mvc.ProblemDetails"></a>
<a id="tocSmicrosoft.aspnetcore.mvc.problemdetails"></a>
<a id="tocsmicrosoft.aspnetcore.mvc.problemdetails"></a>

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|**additionalProperties**|any|false|none|none|
|type|string¦null|false|none|none|
|title|string¦null|false|none|none|
|status|integer(int32)¦null|false|none|none|
|detail|string¦null|false|none|none|
|instance|string¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.JobDetailsResponse">SLP.Services.Domain.Model.JobDetailsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.jobdetailsresponse"></a>
<a id="schema_SLP.Services.Domain.Model.JobDetailsResponse"></a>
<a id="tocSslp.services.domain.model.jobdetailsresponse"></a>
<a id="tocsslp.services.domain.model.jobdetailsresponse"></a>

```json
{
  "cjM_JOB_ID": 0,
  "cjM_JOB_TITLE": "string",
  "customerWorkLocationId": 0,
  "workLocation": "string",
  "latitude": 0.1,
  "longitude": 0.1,
  "customerContactId": 0,
  "firstName": "string",
  "lastName": "string",
  "customerDepartment_Id": 0,
  "departmentName": "string",
  "jlp_Skill_Id": 0,
  "skillName": "string",
  "nuM_OF_POSITIONS": 0,
  "billRate": 0.1,
  "oTrate": 0.1,
  "holidayRate": 0.1,
  "clockInRadius": 0,
  "cityName": "string",
  "stateName": "string",
  "zip": "string",
  "address": "string",
  "cjM_JOB_DETAILS": "string",
  "uniformDescription": "string",
  "projectStartDate": "2019-08-24T14:15:22Z",
  "projectEndDate": "2019-08-24T14:15:22Z",
  "shiftTimingFrom": "string",
  "shiftTimingTo": "string",
  "specialInstructions": "string",
  "jobShiftDetails": [
    {
      "jobShiftDetailId": 0,
      "date": "2019-08-24T14:15:22Z",
      "startTime": "string",
      "endTime": "string",
      "isDeleted": true
    }
  ],
  "reportToLocation": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cjM_JOB_ID|integer(int64)|false|none|none|
|cjM_JOB_TITLE|string¦null|false|none|none|
|customerWorkLocationId|integer(int32)¦null|false|none|none|
|workLocation|string¦null|false|none|none|
|latitude|number(double)¦null|false|none|none|
|longitude|number(double)¦null|false|none|none|
|customerContactId|integer(int32)¦null|false|none|none|
|firstName|string¦null|false|none|none|
|lastName|string¦null|false|none|none|
|customerDepartment_Id|integer(int32)¦null|false|none|none|
|departmentName|string¦null|false|none|none|
|jlp_Skill_Id|integer(int32)¦null|false|none|none|
|skillName|string¦null|false|none|none|
|nuM_OF_POSITIONS|integer(int32)¦null|false|none|none|
|billRate|number(double)¦null|false|none|none|
|oTrate|number(double)¦null|false|none|none|
|holidayRate|number(double)¦null|false|none|none|
|clockInRadius|integer(int32)¦null|false|none|none|
|cityName|string¦null|false|none|none|
|stateName|string¦null|false|none|none|
|zip|string¦null|false|none|none|
|address|string¦null|false|none|none|
|cjM_JOB_DETAILS|string¦null|false|none|none|
|uniformDescription|string¦null|false|none|none|
|projectStartDate|string(date-time)¦null|false|none|none|
|projectEndDate|string(date-time)¦null|false|none|none|
|shiftTimingFrom|string¦null|false|none|none|
|shiftTimingTo|string¦null|false|none|none|
|specialInstructions|string¦null|false|none|none|
|jobShiftDetails|[[SLP.Services.Domain.Model.JobShiftDetailsResponse](#schemaslp.services.domain.model.jobshiftdetailsresponse)]¦null|false|none|none|
|reportToLocation|string¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.JobShiftDetailsResponse">SLP.Services.Domain.Model.JobShiftDetailsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.jobshiftdetailsresponse"></a>
<a id="schema_SLP.Services.Domain.Model.JobShiftDetailsResponse"></a>
<a id="tocSslp.services.domain.model.jobshiftdetailsresponse"></a>
<a id="tocsslp.services.domain.model.jobshiftdetailsresponse"></a>

```json
{
  "jobShiftDetailId": 0,
  "date": "2019-08-24T14:15:22Z",
  "startTime": "string",
  "endTime": "string",
  "isDeleted": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|jobShiftDetailId|integer(int32)|false|none|none|
|date|string(date-time)|false|none|none|
|startTime|string¦null|false|none|none|
|endTime|string¦null|false|none|none|
|isDeleted|boolean|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.AddBusinessWorkLocationModelRequest">SLP.Services.Domain.Model.Request.AddBusinessWorkLocationModelRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.addbusinessworklocationmodelrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.AddBusinessWorkLocationModelRequest"></a>
<a id="tocSslp.services.domain.model.request.addbusinessworklocationmodelrequest"></a>
<a id="tocsslp.services.domain.model.request.addbusinessworklocationmodelrequest"></a>

```json
{
  "customerWorkLocationId": 0,
  "refId": 0,
  "refType": "string",
  "workLocation": "string",
  "latitude": 0.1,
  "longitude": 0.1,
  "address": "string",
  "zip": "string",
  "countryId": 0,
  "stateId": 0,
  "cityId": 0,
  "phoneCode": 0,
  "phone": "string",
  "fax": "string",
  "legalEntityName": "string",
  "title": "string",
  "website": "string",
  "notes": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "billingFirstName": "string",
  "billingLastName": "string",
  "billingAddress": "string",
  "billingCityId": 0,
  "billingStateId": 0,
  "billingZip": "string",
  "billingCountryId": 0,
  "shippingFirstName": "string",
  "shippingLastName": "string",
  "shippingAddress": "string",
  "shippingCityId": 0,
  "shippingStateId": 0,
  "shippingZip": "string",
  "shippingCountryId": 0,
  "role": "string",
  "loginId": 0,
  "unitNumber": "string",
  "clockInRadius": 0,
  "mainPhoneCountryCode": 0,
  "mainPhone": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|customerWorkLocationId|integer(int32)|false|none|none|
|refId|integer(int32)|false|none|none|
|refType|string¦null|false|none|none|
|workLocation|string¦null|false|none|none|
|latitude|number(double)|false|none|none|
|longitude|number(double)|false|none|none|
|address|string¦null|false|none|none|
|zip|string¦null|false|none|none|
|countryId|integer(int32)|false|none|none|
|stateId|integer(int32)|false|none|none|
|cityId|integer(int32)|false|none|none|
|phoneCode|integer(int32)|false|none|none|
|phone|string|true|none|none|
|fax|string¦null|false|none|none|
|legalEntityName|string¦null|false|none|none|
|title|string¦null|false|none|none|
|website|string¦null|false|none|none|
|notes|string¦null|false|none|none|
|firstName|string¦null|false|none|none|
|lastName|string¦null|false|none|none|
|email|string¦null|false|none|none|
|billingFirstName|string¦null|false|none|none|
|billingLastName|string¦null|false|none|none|
|billingAddress|string¦null|false|none|none|
|billingCityId|integer(int32)|false|none|none|
|billingStateId|integer(int32)|false|none|none|
|billingZip|string¦null|false|none|none|
|billingCountryId|integer(int32)|false|none|none|
|shippingFirstName|string¦null|false|none|none|
|shippingLastName|string¦null|false|none|none|
|shippingAddress|string¦null|false|none|none|
|shippingCityId|integer(int32)|false|none|none|
|shippingStateId|integer(int32)|false|none|none|
|shippingZip|string¦null|false|none|none|
|shippingCountryId|integer(int32)|false|none|none|
|role|string¦null|false|none|none|
|loginId|integer(int32)|false|none|none|
|unitNumber|string¦null|false|none|none|
|clockInRadius|integer(int32)¦null|false|none|none|
|mainPhoneCountryCode|integer(int32)|false|none|none|
|mainPhone|string¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.BudgetRequest">SLP.Services.Domain.Model.Request.BudgetRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.budgetrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.BudgetRequest"></a>
<a id="tocSslp.services.domain.model.request.budgetrequest"></a>
<a id="tocsslp.services.domain.model.request.budgetrequest"></a>

```json
{
  "bill_rate": 0.1,
  "currency": "string",
  "unit": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bill_rate|number(double)|false|none|none|
|currency|string¦null|false|none|none|
|unit|integer(int32)¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.Client.AssignContactToWorkLocationRequestModel">SLP.Services.Domain.Model.Request.Client.AssignContactToWorkLocationRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.client.assigncontacttoworklocationrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.Client.AssignContactToWorkLocationRequestModel"></a>
<a id="tocSslp.services.domain.model.request.client.assigncontacttoworklocationrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.client.assigncontacttoworklocationrequestmodel"></a>

```json
{
  "customerContactId": 0,
  "customerWorkLocationId": 0,
  "isDeleted": true,
  "workLocationRoleId": 0,
  "loginId": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|customerContactId|integer(int32)|false|none|none|
|customerWorkLocationId|integer(int32)|false|none|none|
|isDeleted|boolean|false|none|none|
|workLocationRoleId|integer(int32)|false|none|none|
|loginId|integer(int32)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.Client.ClientWorkLocationRequestModel">SLP.Services.Domain.Model.Request.Client.ClientWorkLocationRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.client.clientworklocationrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.Client.ClientWorkLocationRequestModel"></a>
<a id="tocSslp.services.domain.model.request.client.clientworklocationrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.client.clientworklocationrequestmodel"></a>

```json
{
  "intStart": 0,
  "customerID": "string",
  "workLocationSearch": "string",
  "workLocationStatus": 0,
  "intPageSize": 0,
  "intSortColumn": 0,
  "sortDirection": "string",
  "address": "string",
  "contactPerson": "string",
  "contactDetails": "string",
  "isExport": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|intStart|integer(int32)|false|none|none|
|customerID|string¦null|false|none|none|
|workLocationSearch|string¦null|false|none|none|
|workLocationStatus|integer(int32)|false|none|none|
|intPageSize|integer(int32)|false|none|none|
|intSortColumn|integer(int32)|false|none|none|
|sortDirection|string¦null|false|none|none|
|address|string¦null|false|none|none|
|contactPerson|string¦null|false|none|none|
|contactDetails|string¦null|false|none|none|
|isExport|integer(int32)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.Client.DeleteCustomerWorkLocationContactRequestModel">SLP.Services.Domain.Model.Request.Client.DeleteCustomerWorkLocationContactRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.client.deletecustomerworklocationcontactrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.Client.DeleteCustomerWorkLocationContactRequestModel"></a>
<a id="tocSslp.services.domain.model.request.client.deletecustomerworklocationcontactrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.client.deletecustomerworklocationcontactrequestmodel"></a>

```json
{
  "custWorkLocation_ContactId": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|custWorkLocation_ContactId|integer(int32)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.Client.FetchWorkLocationsRequestModel">SLP.Services.Domain.Model.Request.Client.FetchWorkLocationsRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.client.fetchworklocationsrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.Client.FetchWorkLocationsRequestModel"></a>
<a id="tocSslp.services.domain.model.request.client.fetchworklocationsrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.client.fetchworklocationsrequestmodel"></a>

```json
{
  "customerId": 0,
  "searchKey": "string",
  "pageNumber": 0,
  "pageSize": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|customerId|integer(int32)|false|none|none|
|searchKey|string¦null|false|none|none|
|pageNumber|integer(int32)|false|none|none|
|pageSize|integer(int32)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.Client.GetCustomerWLContactsRequestModel">SLP.Services.Domain.Model.Request.Client.GetCustomerWLContactsRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.client.getcustomerwlcontactsrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.Client.GetCustomerWLContactsRequestModel"></a>
<a id="tocSslp.services.domain.model.request.client.getcustomerwlcontactsrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.client.getcustomerwlcontactsrequestmodel"></a>

```json
{
  "intStart": 0,
  "intPageSize": 0,
  "intSortColumn": 0,
  "sortDirection": "string",
  "customerWorkLocationId": 0,
  "customerContactId": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|intStart|integer(int32)|false|none|none|
|intPageSize|integer(int32)|false|none|none|
|intSortColumn|integer(int32)|false|none|none|
|sortDirection|string¦null|false|none|none|
|customerWorkLocationId|integer(int32)¦null|false|none|none|
|customerContactId|integer(int32)¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.CreateJobRequestModel">SLP.Services.Domain.Model.Request.CreateJobRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.createjobrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.CreateJobRequestModel"></a>
<a id="tocSslp.services.domain.model.request.createjobrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.createjobrequestmodel"></a>

```json
{
  "id": 0,
  "templatE_JOB_ID": 0,
  "number_of_openings": 1,
  "jobTitle": "string",
  "department_id": 0,
  "offices": {
    "id": 0,
    "location": {
      "city_name": "string",
      "state_id": 0,
      "country_id": 0
    }
  },
  "requisition_id": "string",
  "start_at": "2019-08-24T14:15:22Z",
  "end_at": "2019-08-24T14:15:22Z",
  "shift_start_time": "string",
  "shift_end_time": "string",
  "notes": "string",
  "status": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "opened_at": "2019-08-24T14:15:22Z",
  "closed_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z",
  "employment_type": "string",
  "budget": {
    "bill_rate": 0.1,
    "currency": "string",
    "unit": 0
  },
  "hiring_managers_id": 0,
  "job_details": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|templatE_JOB_ID|integer(int64)|false|none|none|
|number_of_openings|integer(int32)|true|none|none|
|jobTitle|string|true|none|none|
|department_id|integer(int32)|true|none|none|
|offices|[SLP.Services.Domain.Model.Request.OfficeRequest](#schemaslp.services.domain.model.request.officerequest)|false|none|none|
|requisition_id|string¦null|false|none|none|
|start_at|string(date-time)|true|none|none|
|end_at|string(date-time)|true|none|none|
|shift_start_time|string|true|none|none|
|shift_end_time|string|true|none|none|
|notes|string¦null|false|none|none|
|status|string¦null|false|none|none|
|created_at|string(date-time)|true|none|none|
|opened_at|string(date-time)|true|none|none|
|closed_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|
|employment_type|string|true|none|none|
|budget|[SLP.Services.Domain.Model.Request.BudgetRequest](#schemaslp.services.domain.model.request.budgetrequest)|false|none|none|
|hiring_managers_id|integer(int32)|false|none|none|
|job_details|string|true|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.ForgotPasswordRequest">SLP.Services.Domain.Model.Request.ForgotPasswordRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.forgotpasswordrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.ForgotPasswordRequest"></a>
<a id="tocSslp.services.domain.model.request.forgotpasswordrequest"></a>
<a id="tocsslp.services.domain.model.request.forgotpasswordrequest"></a>

```json
{
  "emailAddress": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|emailAddress|string|true|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.LinkValidRequest">SLP.Services.Domain.Model.Request.LinkValidRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.linkvalidrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.LinkValidRequest"></a>
<a id="tocSslp.services.domain.model.request.linkvalidrequest"></a>
<a id="tocsslp.services.domain.model.request.linkvalidrequest"></a>

```json
{
  "key": "string",
  "type": 1
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|key|string|true|none|none|
|type|integer(int32)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.LocationRequest">SLP.Services.Domain.Model.Request.LocationRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.locationrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.LocationRequest"></a>
<a id="tocSslp.services.domain.model.request.locationrequest"></a>
<a id="tocsslp.services.domain.model.request.locationrequest"></a>

```json
{
  "city_name": "string",
  "state_id": 0,
  "country_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|city_name|string¦null|false|none|none|
|state_id|integer(int32)|false|none|none|
|country_id|integer(int32)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.LoginRequestModel">SLP.Services.Domain.Model.Request.LoginRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.loginrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.LoginRequestModel"></a>
<a id="tocSslp.services.domain.model.request.loginrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.loginrequestmodel"></a>

```json
{
  "email_Id": "user@example.com",
  "password": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email_Id|string(email)|true|none|none|
|password|string|true|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.Master.GetCityListRequest">SLP.Services.Domain.Model.Request.Master.GetCityListRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.master.getcitylistrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.Master.GetCityListRequest"></a>
<a id="tocSslp.services.domain.model.request.master.getcitylistrequest"></a>
<a id="tocsslp.services.domain.model.request.master.getcitylistrequest"></a>

```json
{
  "stateId": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|stateId|integer(int32)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.Master.GetStatesListRequestModel">SLP.Services.Domain.Model.Request.Master.GetStatesListRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.master.getstateslistrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.Master.GetStatesListRequestModel"></a>
<a id="tocSslp.services.domain.model.request.master.getstateslistrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.master.getstateslistrequestmodel"></a>

```json
{
  "intCountry_Id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|intCountry_Id|integer(int32)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.OfficeRequest">SLP.Services.Domain.Model.Request.OfficeRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.officerequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.OfficeRequest"></a>
<a id="tocSslp.services.domain.model.request.officerequest"></a>
<a id="tocsslp.services.domain.model.request.officerequest"></a>

```json
{
  "id": 0,
  "location": {
    "city_name": "string",
    "state_id": 0,
    "country_id": 0
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|location|[SLP.Services.Domain.Model.Request.LocationRequest](#schemaslp.services.domain.model.request.locationrequest)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.RefreshTokenRequest">SLP.Services.Domain.Model.Request.RefreshTokenRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.refreshtokenrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.RefreshTokenRequest"></a>
<a id="tocSslp.services.domain.model.request.refreshtokenrequest"></a>
<a id="tocsslp.services.domain.model.request.refreshtokenrequest"></a>

```json
{
  "accessToken": "string",
  "refreshToken": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|accessToken|string|true|none|none|
|refreshToken|string|true|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.ResetPasswordRequest">SLP.Services.Domain.Model.Request.ResetPasswordRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.resetpasswordrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.ResetPasswordRequest"></a>
<a id="tocSslp.services.domain.model.request.resetpasswordrequest"></a>
<a id="tocsslp.services.domain.model.request.resetpasswordrequest"></a>

```json
{
  "forgotPwdTokenKey": "string",
  "password": "string",
  "confirmPassword": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|forgotPwdTokenKey|string|true|none|none|
|password|string|true|none|none|
|confirmPassword|string|true|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.UpdBudgetRequest">SLP.Services.Domain.Model.Request.UpdBudgetRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.updbudgetrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.UpdBudgetRequest"></a>
<a id="tocSslp.services.domain.model.request.updbudgetrequest"></a>
<a id="tocsslp.services.domain.model.request.updbudgetrequest"></a>

```json
{
  "bill_rate": 0.1,
  "currency": "string",
  "unit": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bill_rate|number(double)|false|none|none|
|currency|string¦null|false|none|none|
|unit|integer(int32)¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.UpdLocationRequest">SLP.Services.Domain.Model.Request.UpdLocationRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.updlocationrequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.UpdLocationRequest"></a>
<a id="tocSslp.services.domain.model.request.updlocationrequest"></a>
<a id="tocsslp.services.domain.model.request.updlocationrequest"></a>

```json
{
  "city_name": "string",
  "state_id": 0,
  "country_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|city_name|string¦null|false|none|none|
|state_id|integer(int32)|false|none|none|
|country_id|integer(int32)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.UpdOfficeRequest">SLP.Services.Domain.Model.Request.UpdOfficeRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.updofficerequest"></a>
<a id="schema_SLP.Services.Domain.Model.Request.UpdOfficeRequest"></a>
<a id="tocSslp.services.domain.model.request.updofficerequest"></a>
<a id="tocsslp.services.domain.model.request.updofficerequest"></a>

```json
{
  "id": 0,
  "location": {
    "city_name": "string",
    "state_id": 0,
    "country_id": 0
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|location|[SLP.Services.Domain.Model.Request.UpdLocationRequest](#schemaslp.services.domain.model.request.updlocationrequest)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Request.UpdateJobRequestModel">SLP.Services.Domain.Model.Request.UpdateJobRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.updatejobrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.UpdateJobRequestModel"></a>
<a id="tocSslp.services.domain.model.request.updatejobrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.updatejobrequestmodel"></a>

```json
{
  "id": 0,
  "template_job_id": 0,
  "number_of_openings": 1,
  "jobTitle": "string",
  "department_id": 0,
  "offices": {
    "id": 0,
    "location": {
      "city_name": "string",
      "state_id": 0,
      "country_id": 0
    }
  },
  "requisition_id": "string",
  "start_at": "2019-08-24T14:15:22Z",
  "end_at": "2019-08-24T14:15:22Z",
  "shift_start_time": "string",
  "shift_end_time": "string",
  "notes": "string",
  "status": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "opened_at": "2019-08-24T14:15:22Z",
  "closed_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z",
  "employment_type": "string",
  "budget": {
    "bill_rate": 0.1,
    "currency": "string",
    "unit": 0
  },
  "hiring_managers_id": 0,
  "job_details": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|template_job_id|integer(int64)|false|none|none|
|number_of_openings|integer(int32)|true|none|none|
|jobTitle|string|true|none|none|
|department_id|integer(int32)|true|none|none|
|offices|[SLP.Services.Domain.Model.Request.UpdOfficeRequest](#schemaslp.services.domain.model.request.updofficerequest)|false|none|none|
|requisition_id|string¦null|false|none|none|
|start_at|string(date-time)|true|none|none|
|end_at|string(date-time)|true|none|none|
|shift_start_time|string|true|none|none|
|shift_end_time|string|true|none|none|
|notes|string¦null|false|none|none|
|status|string¦null|false|none|none|
|created_at|string(date-time)|true|none|none|
|opened_at|string(date-time)|true|none|none|
|closed_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|
|employment_type|string¦null|false|none|none|
|budget|[SLP.Services.Domain.Model.Request.UpdBudgetRequest](#schemaslp.services.domain.model.request.updbudgetrequest)|false|none|none|
|hiring_managers_id|integer(int32)|false|none|none|
|job_details|string|true|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Response.Budget">SLP.Services.Domain.Model.Response.Budget</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.response.budget"></a>
<a id="schema_SLP.Services.Domain.Model.Response.Budget"></a>
<a id="tocSslp.services.domain.model.response.budget"></a>
<a id="tocsslp.services.domain.model.response.budget"></a>

```json
{
  "bill_rate": "string",
  "currency": "string",
  "unit": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bill_rate|string¦null|false|none|none|
|currency|string¦null|false|none|none|
|unit|string¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Response.Department">SLP.Services.Domain.Model.Response.Department</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.response.department"></a>
<a id="schema_SLP.Services.Domain.Model.Response.Department"></a>
<a id="tocSslp.services.domain.model.response.department"></a>
<a id="tocsslp.services.domain.model.response.department"></a>

```json
{
  "id": 0,
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|false|none|none|
|name|string¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Response.EmploymentType">SLP.Services.Domain.Model.Response.EmploymentType</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.response.employmenttype"></a>
<a id="schema_SLP.Services.Domain.Model.Response.EmploymentType"></a>
<a id="tocSslp.services.domain.model.response.employmenttype"></a>
<a id="tocsslp.services.domain.model.response.employmenttype"></a>

```json
{
  "id": "string",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string¦null|false|none|none|
|name|string¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Response.HiringManager">SLP.Services.Domain.Model.Response.HiringManager</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.response.hiringmanager"></a>
<a id="schema_SLP.Services.Domain.Model.Response.HiringManager"></a>
<a id="tocSslp.services.domain.model.response.hiringmanager"></a>
<a id="tocsslp.services.domain.model.response.hiringmanager"></a>

```json
{
  "id": 0,
  "first_Name": "string",
  "last_Name": "string",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|false|none|none|
|first_Name|string¦null|false|none|none|
|last_Name|string¦null|false|none|none|
|name|string¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Response.HiringTeam">SLP.Services.Domain.Model.Response.HiringTeam</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.response.hiringteam"></a>
<a id="schema_SLP.Services.Domain.Model.Response.HiringTeam"></a>
<a id="tocSslp.services.domain.model.response.hiringteam"></a>
<a id="tocsslp.services.domain.model.response.hiringteam"></a>

```json
{
  "hiring_managers": [
    {
      "id": 0,
      "first_Name": "string",
      "last_Name": "string",
      "name": "string"
    }
  ],
  "recruiters": [
    {
      "id": 0,
      "first_Name": "string",
      "last_Name": "string",
      "name": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hiring_managers|[[SLP.Services.Domain.Model.Response.HiringManager](#schemaslp.services.domain.model.response.hiringmanager)]¦null|false|none|none|
|recruiters|[[SLP.Services.Domain.Model.Response.Recruiter](#schemaslp.services.domain.model.response.recruiter)]¦null|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Response.JobByIdResponse">SLP.Services.Domain.Model.Response.JobByIdResponse</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.response.jobbyidresponse"></a>
<a id="schema_SLP.Services.Domain.Model.Response.JobByIdResponse"></a>
<a id="tocSslp.services.domain.model.response.jobbyidresponse"></a>
<a id="tocsslp.services.domain.model.response.jobbyidresponse"></a>

```json
{
  "id": 0,
  "job_title": "string",
  "job_details": "string",
  "requisition_id": "string",
  "status": "string",
  "created_at": "string",
  "opened_at": "string",
  "closed_at": "string",
  "updated_at": "string",
  "number_of_openings": 0,
  "notes": "string",
  "start_at": "string",
  "end_at": "string",
  "shift_start_time": "string",
  "shift_end_time": "string",
  "departments": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "offices": [
    null
  ],
  "employment_type": {
    "id": "string",
    "name": "string"
  },
  "budget": {
    "bill_rate": "string",
    "currency": "string",
    "unit": "string"
  },
  "hiring_team": {
    "hiring_managers": [
      {
        "id": 0,
        "first_Name": "string",
        "last_Name": "string",
        "name": "string"
      }
    ],
    "recruiters": [
      {
        "id": 0,
        "first_Name": "string",
        "last_Name": "string",
        "name": "string"
      }
    ]
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|job_title|string¦null|false|none|none|
|job_details|string¦null|false|none|none|
|requisition_id|string¦null|false|none|none|
|status|string¦null|false|none|none|
|created_at|string¦null|false|none|none|
|opened_at|string¦null|false|none|none|
|closed_at|string¦null|false|none|none|
|updated_at|string¦null|false|none|none|
|number_of_openings|integer(int32)|false|none|none|
|notes|string¦null|false|none|none|
|start_at|string¦null|false|none|none|
|end_at|string¦null|false|none|none|
|shift_start_time|string¦null|false|none|none|
|shift_end_time|string¦null|false|none|none|
|departments|[[SLP.Services.Domain.Model.Response.Department](#schemaslp.services.domain.model.response.department)]¦null|false|none|none|
|offices|[any]¦null|false|none|none|
|employment_type|[SLP.Services.Domain.Model.Response.EmploymentType](#schemaslp.services.domain.model.response.employmenttype)|false|none|none|
|budget|[SLP.Services.Domain.Model.Response.Budget](#schemaslp.services.domain.model.response.budget)|false|none|none|
|hiring_team|[SLP.Services.Domain.Model.Response.HiringTeam](#schemaslp.services.domain.model.response.hiringteam)|false|none|none|

<h2 id="tocS_SLP.Services.Domain.Model.Response.Recruiter">SLP.Services.Domain.Model.Response.Recruiter</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.response.recruiter"></a>
<a id="schema_SLP.Services.Domain.Model.Response.Recruiter"></a>
<a id="tocSslp.services.domain.model.response.recruiter"></a>
<a id="tocsslp.services.domain.model.response.recruiter"></a>

```json
{
  "id": 0,
  "first_Name": "string",
  "last_Name": "string",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|false|none|none|
|first_Name|string¦null|false|none|none|
|last_Name|string¦null|false|none|none|
|name|string¦null|false|none|none|

