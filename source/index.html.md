---
title: VelocityLN Service v1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="slp-service">SLP Service v1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

API Description

<a href="https://velocitymsp.ai">Terms of service</a>
Email: <a href="mailto:support@velocitymsp.ai">Support</a> 
License: <a href="https://velocitymsp.ai/license">Example License</a>

# Authentication

* API Key (Bearer)
    - Parameter Name: **Authorization**, in: header. JWT Authorization header {token}

<h1 id="slp-service-job">Job</h1>

## get__api_Job_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/Job/{id}?api%2Dversion=string \
  -H 'Accept: application/json' \
  -H 'IsATest: undefined' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/Job/{id}?api%2Dversion=string HTTP/1.1

Accept: application/json
IsATest: undefined

```

```javascript

const headers = {
  'Accept':'application/json',
  'IsATest':undefined,
  'Authorization':'API_KEY'
};

fetch('/api/Job/{id}?api%2Dversion=string',
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
  'IsATest' => undefined,
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/Job/{id}',
  params: {
  'api-version' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'IsATest': undefined,
  'Authorization': 'API_KEY'
}

r = requests.get('/api/Job/{id}', params={
  'api-version': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'IsATest' => 'undefined',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/Job/{id}', array(
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
URL obj = new URL("/api/Job/{id}?api%2Dversion=string");
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
        "IsATest": []string{"undefined"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/Job/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/Job/{id}`

*Retrieve details by Id*

<h3 id="get__api_job_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int64)|true|none|
|api-version|query|string|true|none|
|IsATest|header|undefined|false|none|

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

<h3 id="get__api_job_{id}-responses">Responses</h3>

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

## post__api_Job

> Code samples

```shell
# You can also use wget
curl -X POST /api/Job?api%2Dversion=string \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'IsATest: undefined' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/Job?api%2Dversion=string HTTP/1.1

Content-Type: application/json
Accept: application/json
IsATest: undefined

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
  'IsATest':undefined,
  'Authorization':'API_KEY'
};

fetch('/api/Job?api%2Dversion=string',
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
  'IsATest' => undefined,
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/Job',
  params: {
  'api-version' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'IsATest': undefined,
  'Authorization': 'API_KEY'
}

r = requests.post('/api/Job', params={
  'api-version': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'IsATest' => 'undefined',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/Job', array(
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
URL obj = new URL("/api/Job?api%2Dversion=string");
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
        "IsATest": []string{"undefined"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/Job", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/Job`

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

<h3 id="post__api_job-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|api-version|query|string|true|none|
|IsATest|header|undefined|false|none|
|body|body|[SLP.Services.Domain.Model.Request.CreateJobRequestModel](#schemaslp.services.domain.model.request.createjobrequestmodel)|false|none|

> Example responses

> 200 Response

```json
true
```

<h3 id="post__api_job-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|boolean|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get__api_Job

> Code samples

```shell
# You can also use wget
curl -X GET /api/Job?api%2Dversion=string \
  -H 'Accept: application/json' \
  -H 'IsATest: undefined' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/Job?api%2Dversion=string HTTP/1.1

Accept: application/json
IsATest: undefined

```

```javascript

const headers = {
  'Accept':'application/json',
  'IsATest':undefined,
  'Authorization':'API_KEY'
};

fetch('/api/Job?api%2Dversion=string',
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
  'IsATest' => undefined,
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/Job',
  params: {
  'api-version' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'IsATest': undefined,
  'Authorization': 'API_KEY'
}

r = requests.get('/api/Job', params={
  'api-version': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'IsATest' => 'undefined',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/Job', array(
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
URL obj = new URL("/api/Job?api%2Dversion=string");
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
        "IsATest": []string{"undefined"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/Job", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/Job`

*List of jobs based on filter criteria*

<h3 id="get__api_job-parameters">Parameters</h3>

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
|api-version|query|string|true|none|
|IsATest|header|undefined|false|none|

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

<h3 id="get__api_job-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[SLP.Services.Domain.Model.JobDetailsResponse](#schemaslp.services.domain.model.jobdetailsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## patch__api_Job_id

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/Job/id?api%2Dversion=string \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'IsATest: undefined' \
  -H 'Authorization: API_KEY'

```

```http
PATCH /api/Job/id?api%2Dversion=string HTTP/1.1

Content-Type: application/json
Accept: application/json
IsATest: undefined

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
  'IsATest':undefined,
  'Authorization':'API_KEY'
};

fetch('/api/Job/id?api%2Dversion=string',
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
  'IsATest' => undefined,
  'Authorization' => 'API_KEY'
}

result = RestClient.patch '/api/Job/id',
  params: {
  'api-version' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'IsATest': undefined,
  'Authorization': 'API_KEY'
}

r = requests.patch('/api/Job/id', params={
  'api-version': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'IsATest' => 'undefined',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/Job/id', array(
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
URL obj = new URL("/api/Job/id?api%2Dversion=string");
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
        "IsATest": []string{"undefined"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/Job/id", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/Job/id`

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

<h3 id="patch__api_job_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|query|integer(int64)|false|none|
|api-version|query|string|true|none|
|IsATest|header|undefined|false|none|
|body|body|[SLP.Services.Domain.Model.Request.UpdateJobRequestModel](#schemaslp.services.domain.model.request.updatejobrequestmodel)|false|none|

> Example responses

> 200 Response

```json
true
```

<h3 id="patch__api_job_id-responses">Responses</h3>

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

<h1 id="slp-service-login">Login</h1>

## post__api_Login

> Code samples

```shell
# You can also use wget
curl -X POST /api/Login?api%2Dversion=string \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'IsATest: undefined' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/Login?api%2Dversion=string HTTP/1.1

Content-Type: application/json
Accept: application/json
IsATest: undefined

```

```javascript
const inputBody = '{
  "email_Id": "user@example.com",
  "password": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'IsATest':undefined,
  'Authorization':'API_KEY'
};

fetch('/api/Login?api%2Dversion=string',
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
  'IsATest' => undefined,
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/Login',
  params: {
  'api-version' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'IsATest': undefined,
  'Authorization': 'API_KEY'
}

r = requests.post('/api/Login', params={
  'api-version': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'IsATest' => 'undefined',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/Login', array(
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
URL obj = new URL("/api/Login?api%2Dversion=string");
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
        "IsATest": []string{"undefined"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/Login", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/Login`

*User authentication*

> Body parameter

```json
{
  "email_Id": "user@example.com",
  "password": "string"
}
```

<h3 id="post__api_login-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|api-version|query|string|true|none|
|IsATest|header|undefined|false|none|
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

<h3 id="post__api_login-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_Login_RefreshToken

> Code samples

```shell
# You can also use wget
curl -X POST /api/Login/RefreshToken?api%2Dversion=string \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'IsATest: undefined' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/Login/RefreshToken?api%2Dversion=string HTTP/1.1

Content-Type: application/json
Accept: application/json
IsATest: undefined

```

```javascript
const inputBody = '{
  "accessToken": "string",
  "refreshToken": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'IsATest':undefined,
  'Authorization':'API_KEY'
};

fetch('/api/Login/RefreshToken?api%2Dversion=string',
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
  'IsATest' => undefined,
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/Login/RefreshToken',
  params: {
  'api-version' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'IsATest': undefined,
  'Authorization': 'API_KEY'
}

r = requests.post('/api/Login/RefreshToken', params={
  'api-version': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'IsATest' => 'undefined',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/Login/RefreshToken', array(
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
URL obj = new URL("/api/Login/RefreshToken?api%2Dversion=string");
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
        "IsATest": []string{"undefined"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/Login/RefreshToken", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/Login/RefreshToken`

*Refreshes the token.*

> Body parameter

```json
{
  "accessToken": "string",
  "refreshToken": "string"
}
```

<h3 id="post__api_login_refreshtoken-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|api-version|query|string|true|none|
|IsATest|header|undefined|false|none|
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

<h3 id="post__api_login_refreshtoken-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post__api_Login_Logout

> Code samples

```shell
# You can also use wget
curl -X POST /api/Login/Logout?api%2Dversion=string \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'IsATest: undefined' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/Login/Logout?api%2Dversion=string HTTP/1.1

Content-Type: application/json
Accept: application/json
IsATest: undefined

```

```javascript
const inputBody = '{
  "emailId": "user@example.com"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'IsATest':undefined,
  'Authorization':'API_KEY'
};

fetch('/api/Login/Logout?api%2Dversion=string',
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
  'IsATest' => undefined,
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/Login/Logout',
  params: {
  'api-version' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'IsATest': undefined,
  'Authorization': 'API_KEY'
}

r = requests.post('/api/Login/Logout', params={
  'api-version': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'IsATest' => 'undefined',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/Login/Logout', array(
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
URL obj = new URL("/api/Login/Logout?api%2Dversion=string");
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
        "IsATest": []string{"undefined"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/Login/Logout", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/Login/Logout`

*Logouts this instance.*

> Body parameter

```json
{
  "emailId": "user@example.com"
}
```

<h3 id="post__api_login_logout-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|api-version|query|string|true|none|
|IsATest|header|undefined|false|none|
|body|body|[SLP.Services.Domain.Model.Request.LogOutRequestModel](#schemaslp.services.domain.model.request.logoutrequestmodel)|false|none|

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

<h3 id="post__api_login_logout-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Microsoft.AspNetCore.Mvc.ProblemDetails](#schemamicrosoft.aspnetcore.mvc.problemdetails)|
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

<h2 id="tocS_SLP.Services.Domain.Model.Request.LogOutRequestModel">SLP.Services.Domain.Model.Request.LogOutRequestModel</h2>
<!-- backwards compatibility -->
<a id="schemaslp.services.domain.model.request.logoutrequestmodel"></a>
<a id="schema_SLP.Services.Domain.Model.Request.LogOutRequestModel"></a>
<a id="tocSslp.services.domain.model.request.logoutrequestmodel"></a>
<a id="tocsslp.services.domain.model.request.logoutrequestmodel"></a>

```json
{
  "emailId": "user@example.com"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|emailId|string(email)|true|none|none|

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

