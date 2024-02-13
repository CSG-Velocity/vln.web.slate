{ "openapi": "3.0.1", "info": { "title": "SLP Service1.0",
"description": "API Description", "termsOfService":
"https://velocitymsp.ai", "contact": { "name": "Support", "email":
"support@velocitymsp.ai" }, "license": { "name": "Example License",
"url": "https://velocitymsp.ai/license1" }, "version": "1.0" }, "paths":
{ "/api/v1/Client/AddBusinessWorkLocation": { "post": { "tags": \[
"Client" \], "requestBody": { "content": { "application/json": {
"schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.AddBusinessWorkLocationModelRequest"  }  },  "text/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.AddBusinessWorkLocationModelRequest"
} }, "application/*+json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.AddBusinessWorkLocationModelRequest"  }  }  }  },  "responses": {  "201": {  "description": "Created"  },  "500": {  "description": "Server Error"  },  "400": {  "description": "Bad Request",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } } } },
"417": { "description": "Client Error", "content": { "application/json":
{ "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  }  }  }  },  "/api/v1/Client/FetchWorkLocations": {  "post": {  "tags": [  "Client"  ],  "requestBody": {  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.Client.FetchWorkLocationsRequestModel"
} }, "text/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.Client.FetchWorkLocationsRequestModel"  }  },  "application/*+json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.Client.FetchWorkLocationsRequestModel"
} } } }, "responses": { "200": { "description": "Success" }, "500": {
"description": "Server Error" }, "400": { "description": "Bad Request",
"content": { "application/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  }  }  }  },  "/api/v1/Client/AssignContactToWorkLocation": {  "post": {  "tags": [  "Client"  ],  "requestBody": {  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.Client.AssignContactToWorkLocationRequestModel"
} }, "text/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.Client.AssignContactToWorkLocationRequestModel"  }  },  "application/*+json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.Client.AssignContactToWorkLocationRequestModel"
} } } }, "responses": { "200": { "description": "Success" }, "500": {
"description": "Server Error" }, "400": { "description": "Bad Request",
"content": { "application/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  }  }  }  },  "/api/v1/Job/TestVersioning": {  "get": {  "tags": [  "Job"  ],  "responses": {  "200": {  "description": "Success",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Response.JobByIdResponse"
} } } } } } }, "/api/v1/Job/{id}": { "get": { "tags": \[ "Job" \],
"summary": "Retrieve details by Id", "parameters": \[ { "name": "id",
"in": "path", "description": "", "required": true, "schema": { "type":
"integer", "format": "int64" } } \], "responses": { "200": {
"description": "Success", "content": { "application/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Response.JobByIdResponse"  }  }  }  },  "404": {  "description": "Not Found",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } } } },
"500": { "description": "Server Error" }, "400": { "description": "Bad
Request", "content": { "application/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  }  }  }  },  "/api/v1/Job": {  "post": {  "tags": [  "Job"  ],  "summary": "Create a new Job",  "requestBody": {  "description": "",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.CreateJobRequestModel"
} }, "text/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.CreateJobRequestModel"  }  },  "application/*+json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.CreateJobRequestModel"
} } } }, "responses": { "200": { "description": "Success", "content": {
"application/json": { "schema": { "type": "boolean" } } } }, "500": {
"description": "Server Error" }, "400": { "description": "Bad Request",
"content": { "application/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  }  }  },  "get": {  "tags": [  "Job"  ],  "summary": "List of jobs based on filter criteria",  "parameters": [  {  "name": "IntStart",  "in": "query",  "schema": {  "type": "integer",  "format": "int32"  }  },  {  "name": "IntPageSize",  "in": "query",  "schema": {  "type": "integer",  "format": "int32"  }  },  {  "name": "IntSortColumn",  "in": "query",  "schema": {  "type": "integer",  "format": "int32"  }  },  {  "name": "SortDirection",  "in": "query",  "schema": {  "type": "string"  }  },  {  "name": "Created_before",  "in": "query",  "schema": {  "type": "string"  }  },  {  "name": "Created_after",  "in": "query",  "schema": {  "type": "string"  }  },  {  "name": "Updated_before",  "in": "query",  "schema": {  "type": "string"  }  },  {  "name": "Updated_after",  "in": "query",  "schema": {  "type": "string"  }  },  {  "name": "Status",  "in": "query",  "schema": {  "type": "string"  }  },  {  "name": "DepartmentId",  "in": "query",  "schema": {  "type": "integer",  "format": "int32"  }  },  {  "name": "OfficeId",  "in": "query",  "schema": {  "type": "integer",  "format": "int32"  }  }  ],  "responses": {  "200": {  "description": "Success",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.JobDetailsResponse" } }
} }, "500": { "description": "Server Error" }, "400": { "description":
"Bad Request", "content": { "application/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  }  }  }  },  "/api/v1/Job/id": {  "patch": {  "tags": [  "Job"  ],  "summary": "Update an existing Job",  "parameters": [  {  "name": "id",  "in": "query",  "description": "",  "schema": {  "type": "integer",  "format": "int64"  }  }  ],  "requestBody": {  "description": "",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.UpdateJobRequestModel"
} }, "text/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.UpdateJobRequestModel"  }  },  "application/*+json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.UpdateJobRequestModel"
} } } }, "responses": { "200": { "description": "Success", "content": {
"application/json": { "schema": { "type": "boolean" } } } }, "500": {
"description": "Server Error" }, "400": { "description": "Bad Request",
"content": { "application/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  },  "404": {  "description": "Not Found",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } } } } }
} }, "/api/v1/Login": { "post": { "tags": \[ "Login" \], "summary":
"User authentication", "requestBody": { "description": "", "content": {
"application/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.LoginRequestModel"  }  },  "text/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.LoginRequestModel"
} }, "application/*+json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.LoginRequestModel"  }  }  }  },  "responses": {  "200": {  "description": "Success"  },  "400": {  "description": "Bad Request",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } } } },
"500": { "description": "Server Error" } } } },
"/api/v1/Login/RefreshToken": { "post": { "tags": \[ "Login" \],
"summary": "Refreshes the token.", "requestBody": { "description": "The
refresh request.", "content": { "application/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.RefreshTokenRequest"  }  },  "text/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.RefreshTokenRequest"
} }, "application/*+json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.RefreshTokenRequest"  }  }  }  },  "responses": {  "200": {  "description": "Success"  },  "400": {  "description": "Bad Request",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } } } },
"500": { "description": "Server Error" } } } }, "/api/v1/Login/Logout":
{ "post": { "tags": \[ "Login" \], "summary": "Logouts this instance.",
"requestBody": { "content": { "application/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.LogOutRequestModel"  }  },  "text/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.LogOutRequestModel"
} }, "application/*+json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.LogOutRequestModel"  }  }  }  },  "responses": {  "200": {  "description": "Success"  },  "400": {  "description": "Bad Request",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } } } },
"500": { "description": "Server Error" } } } },
"/api/v1/Login/EmailValidation": { "get": { "tags": \[ "Login" \],
"summary": "User will enter email for login process", "parameters": \[ {
"name": "EmailId", "in": "query", "required": true, "schema": { "type":
"string", "format": "email" } } \], "responses": { "200": {
"description": "Success" }, "400": { "description": "Bad Request",
"content": { "application/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  },  "500": {  "description": "Server Error"  }  }  }  },  "/api/v1/Login/ForgotPassword": {  "post": {  "tags": [  "Login"  ],  "summary": "Forgots the password.",  "requestBody": {  "description": "The request.",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.ForgotPasswordRequest"
} }, "text/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.ForgotPasswordRequest"  }  },  "application/*+json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.ForgotPasswordRequest"
} } } }, "responses": { "200": { "description": "Success" }, "400": {
"description": "Bad Request", "content": { "application/json": {
"schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  },  "500": {  "description": "Server Error"  }  }  }  },  "/api/v1/Login/IsForgetPasswordLinkValid": {  "post": {  "tags": [  "Login"  ],  "summary": "To Validate Forget password link",  "requestBody": {  "description": "",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.LinkValidRequest"
} }, "text/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.LinkValidRequest"  }  },  "application/*+json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.LinkValidRequest"
} } } }, "responses": { "200": { "description": "Success" }, "400": {
"description": "Bad Request", "content": { "application/json": {
"schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  },  "404": {  "description": "Not Found",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } } } },
"500": { "description": "Server Error" } } } },
"/api/v1/Login/ResetPassword": { "post": { "tags": \[ "Login" \],
"requestBody": { "content": { "application/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.ResetPasswordRequest"  }  },  "text/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.ResetPasswordRequest"
} }, "application/\*+json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.ResetPasswordRequest"  }  }  }  },  "responses": {  "200": {  "description": "Success"  },  "400": {  "description": "Bad Request",  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } } } },
"500": { "description": "Server Error" } } } },
"/api/v1/Master/GetCountryList": { "get": { "tags": \[ "Master" \],
"parameters": \[ { "name": "intCountryId", "in": "query", "schema": {
"type": "integer", "format": "int32", "default": 0 } }, { "name":
"strCountryCode", "in": "query", "schema": { "type": "string",
"default": "" } } \], "responses": { "200": { "description": "Success"
}, "500": { "description": "Server Error" }, "417": { "description":
"Client Error", "content": { "text/plain": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  },  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } },
"text/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  }  }  }  },  "/api/v1/Master/GetStatesListByCountryId": {  "post": {  "tags": [  "Master"  ],  "requestBody": {  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.Master.GetStatesListRequestModel"
} }, "text/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.Master.GetStatesListRequestModel"  }  },  "application/*+json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.Master.GetStatesListRequestModel"
} } } }, "responses": { "200": { "description": "Success" }, "500": {
"description": "Server Error" }, "417": { "description": "Client Error",
"content": { "text/plain": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  },  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } },
"text/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  }  }  }  },  "/api/v1/Master/GetCityListByStateId": {  "post": {  "tags": [  "Master"  ],  "requestBody": {  "content": {  "application/json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.Master.GetCityListRequest"
} }, "text/json": { "schema": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.Master.GetCityListRequest"  }  },  "application/*+json": {  "schema": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.Master.GetCityListRequest"
} } } }, "responses": { "200": { "description": "Success" }, "500": {
"description": "Server Error" }, "417": { "description": "Client Error",
"content": { "text/plain": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  },  "application/json": {  "schema": {  "$ref":
"#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails" } },
"text/json": { "schema": {
"$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"  }  }  }  }  }  }  }  },  "components": {  "schemas": {  "Microsoft.AspNetCore.Mvc.ProblemDetails": {  "type": "object",  "properties": {  "type": {  "type": "string",  "nullable": true  },  "title": {  "type": "string",  "nullable": true  },  "status": {  "type": "integer",  "format": "int32",  "nullable": true  },  "detail": {  "type": "string",  "nullable": true  },  "instance": {  "type": "string",  "nullable": true  }  },  "additionalProperties": { }  },  "SLP.Services.Domain.Model.JobDetailsResponse": {  "type": "object",  "properties": {  "cjM_JOB_ID": {  "type": "integer",  "format": "int64"  },  "cjM_JOB_TITLE": {  "type": "string",  "nullable": true  },  "customerWorkLocationId": {  "type": "integer",  "format": "int32",  "nullable": true  },  "workLocation": {  "type": "string",  "nullable": true  },  "latitude": {  "type": "number",  "format": "double",  "nullable": true  },  "longitude": {  "type": "number",  "format": "double",  "nullable": true  },  "customerContactId": {  "type": "integer",  "format": "int32",  "nullable": true  },  "firstName": {  "type": "string",  "nullable": true  },  "lastName": {  "type": "string",  "nullable": true  },  "customerDepartment_Id": {  "type": "integer",  "format": "int32",  "nullable": true  },  "departmentName": {  "type": "string",  "nullable": true  },  "jlp_Skill_Id": {  "type": "integer",  "format": "int32",  "nullable": true  },  "skillName": {  "type": "string",  "nullable": true  },  "nuM_OF_POSITIONS": {  "type": "integer",  "format": "int32",  "nullable": true  },  "billRate": {  "type": "number",  "format": "double",  "nullable": true  },  "oTrate": {  "type": "number",  "format": "double",  "nullable": true  },  "holidayRate": {  "type": "number",  "format": "double",  "nullable": true  },  "clockInRadius": {  "type": "integer",  "format": "int32",  "nullable": true  },  "cityName": {  "type": "string",  "nullable": true  },  "stateName": {  "type": "string",  "nullable": true  },  "zip": {  "type": "string",  "nullable": true  },  "address": {  "type": "string",  "nullable": true  },  "cjM_JOB_DETAILS": {  "type": "string",  "nullable": true  },  "uniformDescription": {  "type": "string",  "nullable": true  },  "projectStartDate": {  "type": "string",  "format": "date-time",  "nullable": true  },  "projectEndDate": {  "type": "string",  "format": "date-time",  "nullable": true  },  "shiftTimingFrom": {  "type": "string",  "nullable": true  },  "shiftTimingTo": {  "type": "string",  "nullable": true  },  "specialInstructions": {  "type": "string",  "nullable": true  },  "jobShiftDetails": {  "type": "array",  "items": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.JobShiftDetailsResponse"
}, "nullable": true }, "reportToLocation": { "type": "string",
"nullable": true } }, "additionalProperties": false },
"SLP.Services.Domain.Model.JobShiftDetailsResponse": { "type": "object",
"properties": { "jobShiftDetailId": { "type": "integer", "format":
"int32" }, "date": { "type": "string", "format": "date-time" },
"startTime": { "type": "string", "nullable": true }, "endTime": {
"type": "string", "nullable": true }, "isDeleted": { "type": "boolean" }
}, "additionalProperties": false },
"SLP.Services.Domain.Model.Request.AddBusinessWorkLocationModelRequest":
{ "required": \[ "phone" \], "type": "object", "properties": {
"customerWorkLocationId": { "type": "integer", "format": "int32" },
"refId": { "type": "integer", "format": "int32" }, "refType": { "type":
"string", "nullable": true }, "workLocation": { "type": "string",
"nullable": true }, "latitude": { "type": "number", "format": "double"
}, "longitude": { "type": "number", "format": "double" }, "address": {
"type": "string", "nullable": true }, "zip": { "type": "string",
"nullable": true }, "countryId": { "type": "integer", "format": "int32"
}, "stateId": { "type": "integer", "format": "int32" }, "cityId": {
"type": "integer", "format": "int32" }, "phoneCode": { "type":
"integer", "format": "int32" }, "phone": { "minLength": 1, "type":
"string" }, "fax": { "type": "string", "nullable": true },
"legalEntityName": { "type": "string", "nullable": true }, "title": {
"type": "string", "nullable": true }, "website": { "type": "string",
"nullable": true }, "notes": { "type": "string", "nullable": true },
"firstName": { "type": "string", "nullable": true }, "lastName": {
"type": "string", "nullable": true }, "email": { "type": "string",
"nullable": true }, "billingFirstName": { "type": "string", "nullable":
true }, "billingLastName": { "type": "string", "nullable": true },
"billingAddress": { "type": "string", "nullable": true },
"billingCityId": { "type": "integer", "format": "int32" },
"billingStateId": { "type": "integer", "format": "int32" },
"billingZip": { "type": "string", "nullable": true },
"billingCountryId": { "type": "integer", "format": "int32" },
"shippingFirstName": { "type": "string", "nullable": true },
"shippingLastName": { "type": "string", "nullable": true },
"shippingAddress": { "type": "string", "nullable": true },
"shippingCityId": { "type": "integer", "format": "int32" },
"shippingStateId": { "type": "integer", "format": "int32" },
"shippingZip": { "type": "string", "nullable": true },
"shippingCountryId": { "type": "integer", "format": "int32" }, "role": {
"type": "string", "nullable": true }, "loginId": { "type": "integer",
"format": "int32" }, "unitNumber": { "type": "string", "nullable": true
}, "clockInRadius": { "type": "integer", "format": "int32", "nullable":
true }, "mainPhoneCountryCode": { "type": "integer", "format": "int32"
}, "mainPhone": { "type": "string", "nullable": true } },
"additionalProperties": false },
"SLP.Services.Domain.Model.Request.BudgetRequest": { "type": "object",
"properties": { "bill_rate": { "type": "number", "format": "double" },
"currency": { "type": "string", "nullable": true }, "unit": { "type":
"integer", "format": "int32", "nullable": true } },
"additionalProperties": false },
"SLP.Services.Domain.Model.Request.Client.AssignContactToWorkLocationRequestModel":
{ "type": "object", "properties": { "customerContactId": { "type":
"integer", "format": "int32" }, "customerWorkLocationId": { "type":
"integer", "format": "int32" }, "isDeleted": { "type": "boolean" },
"workLocationRoleId": { "type": "integer", "format": "int32" },
"loginId": { "type": "integer", "format": "int32" } },
"additionalProperties": false },
"SLP.Services.Domain.Model.Request.Client.FetchWorkLocationsRequestModel":
{ "type": "object", "properties": { "customerId": { "type": "integer",
"format": "int32" }, "searchKey": { "type": "string", "nullable": true
}, "pageNumber": { "type": "integer", "format": "int32" }, "pageSize": {
"type": "integer", "format": "int32" } }, "additionalProperties": false
}, "SLP.Services.Domain.Model.Request.CreateJobRequestModel": {
"required": \[ "created_at", "department_id", "employment_type",
"end_at", "job_details", "jobTitle", "number_of_openings", "opened_at",
"shift_end_time", "shift_start_time", "start_at" \], "type": "object",
"properties": { "id": { "type": "integer", "format": "int64" },
"templatE_JOB_ID": { "type": "integer", "format": "int64" },
"number_of_openings": { "maximum": 2147483647, "minimum": 1, "type":
"integer", "format": "int32" }, "jobTitle": { "minLength": 1, "type":
"string" }, "department_id": { "type": "integer", "format": "int32" },
"offices": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.OfficeRequest"  },  "requisition_id": {  "type": "string",  "nullable": true  },  "start_at": {  "type": "string",  "format": "date-time"  },  "end_at": {  "type": "string",  "format": "date-time"  },  "shift_start_time": {  "minLength": 1,  "type": "string"  },  "shift_end_time": {  "minLength": 1,  "type": "string"  },  "notes": {  "type": "string",  "nullable": true  },  "status": {  "type": "string",  "nullable": true  },  "created_at": {  "type": "string",  "format": "date-time"  },  "opened_at": {  "type": "string",  "format": "date-time"  },  "closed_at": {  "type": "string",  "format": "date-time"  },  "updated_at": {  "type": "string",  "format": "date-time"  },  "employment_type": {  "minLength": 1,  "type": "string"  },  "budget": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.BudgetRequest"
}, "hiring_managers_id": { "type": "integer", "format": "int32" },
"job_details": { "minLength": 1, "type": "string" } },
"additionalProperties": false },
"SLP.Services.Domain.Model.Request.ForgotPasswordRequest": { "required":
\[ "emailAddress" \], "type": "object", "properties": { "emailAddress":
{ "minLength": 1, "type": "string" } }, "additionalProperties": false },
"SLP.Services.Domain.Model.Request.LinkValidRequest": { "required": \[
"key" \], "type": "object", "properties": { "key": { "minLength": 1,
"type": "string" }, "type": { "maximum": 2147483647, "minimum": 1,
"type": "integer", "format": "int32" } }, "additionalProperties": false
}, "SLP.Services.Domain.Model.Request.LocationRequest": { "type":
"object", "properties": { "city_name": { "type": "string", "nullable":
true }, "state_id": { "type": "integer", "format": "int32" },
"country_id": { "type": "integer", "format": "int32" } },
"additionalProperties": false },
"SLP.Services.Domain.Model.Request.LogOutRequestModel": { "required": \[
"emailId" \], "type": "object", "properties": { "emailId": {
"minLength": 1, "type": "string", "format": "email" } },
"additionalProperties": false },
"SLP.Services.Domain.Model.Request.LoginRequestModel": { "required": \[
"email_Id", "password" \], "type": "object", "properties": { "email_Id":
{ "minLength": 1, "type": "string", "format": "email" }, "password": {
"minLength": 1, "type": "string" } }, "additionalProperties": false },
"SLP.Services.Domain.Model.Request.Master.GetCityListRequest": { "type":
"object", "properties": { "stateId": { "type": "integer", "format":
"int32" } }, "additionalProperties": false },
"SLP.Services.Domain.Model.Request.Master.GetStatesListRequestModel": {
"type": "object", "properties": { "intCountry_Id": { "type": "integer",
"format": "int32" } }, "additionalProperties": false },
"SLP.Services.Domain.Model.Request.OfficeRequest": { "type": "object",
"properties": { "id": { "type": "integer", "format": "int64" },
"location": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.LocationRequest"  }  },  "additionalProperties": false  },  "SLP.Services.Domain.Model.Request.RefreshTokenRequest": {  "required": [  "accessToken",  "refreshToken"  ],  "type": "object",  "properties": {  "accessToken": {  "minLength": 1,  "type": "string"  },  "refreshToken": {  "minLength": 1,  "type": "string"  }  },  "additionalProperties": false  },  "SLP.Services.Domain.Model.Request.ResetPasswordRequest": {  "required": [  "confirmPassword",  "forgotPwdTokenKey",  "password"  ],  "type": "object",  "properties": {  "forgotPwdTokenKey": {  "minLength": 1,  "type": "string"  },  "password": {  "minLength": 1,  "type": "string"  },  "confirmPassword": {  "minLength": 1,  "type": "string"  }  },  "additionalProperties": false  },  "SLP.Services.Domain.Model.Request.UpdBudgetRequest": {  "type": "object",  "properties": {  "bill_rate": {  "type": "number",  "format": "double"  },  "currency": {  "type": "string",  "nullable": true  },  "unit": {  "type": "integer",  "format": "int32",  "nullable": true  }  },  "additionalProperties": false  },  "SLP.Services.Domain.Model.Request.UpdLocationRequest": {  "type": "object",  "properties": {  "city_name": {  "type": "string",  "nullable": true  },  "state_id": {  "type": "integer",  "format": "int32"  },  "country_id": {  "type": "integer",  "format": "int32"  }  },  "additionalProperties": false  },  "SLP.Services.Domain.Model.Request.UpdOfficeRequest": {  "type": "object",  "properties": {  "id": {  "type": "integer",  "format": "int64"  },  "location": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.UpdLocationRequest"
} }, "additionalProperties": false },
"SLP.Services.Domain.Model.Request.UpdateJobRequestModel": { "required":
\[ "created_at", "department_id", "end_at", "job_details", "jobTitle",
"number_of_openings", "opened_at", "shift_end_time", "shift_start_time",
"start_at" \], "type": "object", "properties": { "id": { "type":
"integer", "format": "int64" }, "template_job_id": { "type": "integer",
"format": "int64" }, "number_of_openings": { "maximum": 2147483647,
"minimum": 1, "type": "integer", "format": "int32" }, "jobTitle": {
"minLength": 1, "type": "string" }, "department_id": { "type":
"integer", "format": "int32" }, "offices": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Request.UpdOfficeRequest"  },  "requisition_id": {  "type": "string",  "nullable": true  },  "start_at": {  "type": "string",  "format": "date-time"  },  "end_at": {  "type": "string",  "format": "date-time"  },  "shift_start_time": {  "minLength": 1,  "type": "string"  },  "shift_end_time": {  "minLength": 1,  "type": "string"  },  "notes": {  "type": "string",  "nullable": true  },  "status": {  "type": "string",  "nullable": true  },  "created_at": {  "type": "string",  "format": "date-time"  },  "opened_at": {  "type": "string",  "format": "date-time"  },  "closed_at": {  "type": "string",  "format": "date-time"  },  "updated_at": {  "type": "string",  "format": "date-time"  },  "employment_type": {  "type": "string",  "nullable": true  },  "budget": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Request.UpdBudgetRequest"
}, "hiring_managers_id": { "type": "integer", "format": "int32" },
"job_details": { "minLength": 1, "type": "string" } },
"additionalProperties": false },
"SLP.Services.Domain.Model.Response.Budget": { "type": "object",
"properties": { "bill_rate": { "type": "string", "nullable": true },
"currency": { "type": "string", "nullable": true }, "unit": { "type":
"string", "nullable": true } }, "additionalProperties": false },
"SLP.Services.Domain.Model.Response.Department": { "type": "object",
"properties": { "id": { "type": "integer", "format": "int32" }, "name":
{ "type": "string", "nullable": true } }, "additionalProperties": false
}, "SLP.Services.Domain.Model.Response.EmploymentType": { "type":
"object", "properties": { "id": { "type": "string", "nullable": true },
"name": { "type": "string", "nullable": true } },
"additionalProperties": false },
"SLP.Services.Domain.Model.Response.HiringManager": { "type": "object",
"properties": { "id": { "type": "integer", "format": "int32" },
"first_Name": { "type": "string", "nullable": true }, "last_Name": {
"type": "string", "nullable": true }, "name": { "type": "string",
"nullable": true } }, "additionalProperties": false },
"SLP.Services.Domain.Model.Response.HiringTeam": { "type": "object",
"properties": { "hiring_managers": { "type": "array", "items": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Response.HiringManager"  },  "nullable": true  },  "recruiters": {  "type": "array",  "items": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Response.Recruiter" },
"nullable": true } }, "additionalProperties": false },
"SLP.Services.Domain.Model.Response.JobByIdResponse": { "type":
"object", "properties": { "id": { "type": "integer", "format": "int64"
}, "job_title": { "type": "string", "nullable": true }, "job_details": {
"type": "string", "nullable": true }, "requisition_id": { "type":
"string", "nullable": true }, "status": { "type": "string", "nullable":
true }, "created_at": { "type": "string", "nullable": true },
"opened_at": { "type": "string", "nullable": true }, "closed_at": {
"type": "string", "nullable": true }, "updated_at": { "type": "string",
"nullable": true }, "number_of_openings": { "type": "integer", "format":
"int32" }, "notes": { "type": "string", "nullable": true }, "start_at":
{ "type": "string", "nullable": true }, "end_at": { "type": "string",
"nullable": true }, "shift_start_time": { "type": "string", "nullable":
true }, "shift_end_time": { "type": "string", "nullable": true },
"departments": { "type": "array", "items": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Response.Department"  },  "nullable": true  },  "offices": {  "type": "array",  "items": { },  "nullable": true  },  "employment_type": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Response.EmploymentType"
}, "budget": {
"$ref": "#/components/schemas/SLP.Services.Domain.Model.Response.Budget"  },  "hiring_team": {  "$ref":
"#/components/schemas/SLP.Services.Domain.Model.Response.HiringTeam" }
}, "additionalProperties": false },
"SLP.Services.Domain.Model.Response.Recruiter": { "type": "object",
"properties": { "id": { "type": "integer", "format": "int32" },
"first_Name": { "type": "string", "nullable": true }, "last_Name": {
"type": "string", "nullable": true }, "name": { "type": "string",
"nullable": true } }, "additionalProperties": false } },
"securitySchemes": { "Bearer": { "type": "apiKey", "description": "JWT
Authorization header {token}", "name": "Authorization", "in": "header" }
} }, "security": \[ { "Bearer": \[ \] } \] }
