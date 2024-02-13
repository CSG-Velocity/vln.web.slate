# Introduction

```
  _          _ _
 | |__   ___| | | ___
 | '_ \ / _ \ | |/ _ \
 | | | |  __/ | | (_) |
 |_| |_|\___|_|_|\___/     _
 __      _____  _ __| | __| |
 \ \ /\ / / _ \| '__| |/ _` |
  \ V  V / (_) | |  | | (_| |
   \_/\_/ \___/|_|  |_|\__,_|
```

With Velocity Lean, you have access to most of your Velocity Lean data!

The Velocity Lean API was designed to allow our customers to manage their data from Velocity Lean. However, it can also be used to...

1.  Update candidate information.
2.  Add attachments to candidate profiles.
3.  Advance, move, and reject applications.
4.  Add or update a job opening.
5.  Add application to candidate and many more...

We have usage examples for cURL! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

This documentation is open source!

## Authentication

> To authorize, use this code:

```ruby
require 'base64'
secret = 'a7183e1b7e9ab09b8a5cfa87d1934c3c'
credential = Base64.strict_encode64(secret + ':')
# => "YTcxODNlMWI3ZTlhYjA5YjhhNWNmYTg3ZDE5MzRjM2M6"

headers = {
  "Authorization" => "Basic " + credential
}
```

```shell
# Note the trailing colon after the username (API token):
$ curl https://api.Velocityln.io/v1/ -u a7183e1b7e9ab09b8a5cfa87d1934c3c:
...

> GET /v1/ HTTP/1.1
> Host: api.velocityln.ai
> Authorization: Basic YTcxODNlMWI3ZTlhYjA5YjhhNWNmYTg3ZDE5MzRjM2M6

...
```

Velocity Lean uses Basic Auth over HTTPS for authentication. The username is your VelocityFx API token and the password should be blank. Unauthenticated requests will return an HTTP 401 response.

Velocity Lean API keys can be obtained in VelocityFx. In order to create a Velocity Lean API key, a user must be granted the "Can manage ALL organization's API Credentials" in the "Developer permission" section. That user can then go Configure >> Dev Center >> API Credential Management. From there, you can create a Velocity Lean API key and choose which endpoints it may access.

**Important Note:** Users with Velocity Lean API keys may access all the data in the endpoint. Access to data in Velocity Lean is binary: everything or nothing. Velocity Lean API keys should be given to internal developers with this understanding and to third parties with caution. Each key should only be allowed to access the endpoints it absolutely needs.

### Authorization header

> Your `Authorization` header should look like this:

```
Authorization: Basic YTcxODNlMWI3ZTlhYjA5YjhhNWNmYTg3ZDE5MzRjM2M6
```

Most HTTP clients will automatically use a given username and password to generate the required Authorization header. However, you may need to explicity set this header. The header has the following format:

`Authorization: Basic <base64("username:password")>`

Since only a username needs to be provided in our case, you'll need to append a `:` (colon) to your VelocityFx API token and then Base64 encode the resulting string.

<aside class="success">
<b>Important</b>: Use HTTPS for all requests. Requests made over HTTP will always return an HTTP 403 response. Keep your API key a secret!
</aside>

### Setting credentials with cURL

If you're making test API requests with cURL you can use the `-u` flag to set the username and password (which is blank). cURL will automatically generate the `Authorization` header.

### Setting permissions for API Keys

You can specify which API endpoints your API keys have access to from the VelocityFx Dev Center. This will allow you to permit or deny access to each endpoint individually. 

To add or remove endpoint permissions on an API key, go to the Dev Center in VelocityFx, click "API Credential Management," then click "Manage Permissions" next to your Velocity Lean API Key. From there, check or uncheck permissions for any endpoints.

## Rate limiting

```
Status: 200 OK
X-RateLimit-Limit: 50
X-RateLimit-Remaining: 49
```

Velocity Lean API requests are limited to the amount specified in the returned `X-RateLimit-Limit` header, per 10 seconds. Check the `X-RateLimit-Limit` and `X-RateLimit-Remaining` headers to see how many more requests are permitted before you're throttled. Exceeding the limit will return an `HTTP 429` response. In the `HTTP 429` response, the `Retry-After` header includes an Epoch / Unix timestamp indicating when you can try again.

## Pagination

> Example paging header

```
Link: <https://api.Velocityln.ai/v1?page=2&per_page=2>; rel="next",
<https://api.Velocityln.ai/v1?page=474&per_page=2>; rel="last"
```

API methods that return a collection of results are always paginated. Paginated results will include a `Link` (see [RFC-5988](https://tools.ietf.org/html/rfc5988)) response header with the following information.

- `next`. The corresponding URL is the link to the next page.

Note that when this header is not set, there is only one page, the first page, of results.

<aside class="warning">Since paging mechanisms may differ per paginated endpoint and may change in the future, it is important to use the Link headers and not page manually by changing the paging-related query parameters.</aside>

## Validation

```json
{
  "message": "Validation error",
  "errors": [
    {
      "message": "Must be one of: legal entity",
      "field": "type"
    }
  ]
}
```

Methods that take input will validate all parameters. Any parameter that fails validation will trigger an error response with status `HTTP 422`. The response body will be a JSON object that includes a message as well as a list of fields that failed validation.

## General considerations

Unless otherwise specified, API methods generally conform to the following:

- Properties without a value will use `null` instead of being undefined
- "Snake Case" is used for attribute names (e.g. `first_name`)
- Timestamps are rendered in ISO-8601 format (e.g. `2016-02-03T16:38:46.985Z)
- URLs to external resources are valid for 7 days
- We reserve the right to add more properties to objects, but will never change or remove them
- Resumes, cover letters, and other document attachments in VelocityFx are hosted on Azure blob storage and are provided via signed, temporary URLs. Due to the ephemeral nature of these resource links, users should download these documents immediately after the request is made and should not rely on these URLs to be available for future requests. In the event Azure blob storage is experiencing issues, document attachments will not be available in Velocity Lean.

## Errors

| Error Code | Meaning                                                                                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 401        | Unauthorized – Ensure you’re using a valid Velocity Lean API key with the correct permissions in the `Authorization` header (Basic Auth).                   |
| 403        | Forbidden -- You don't have access to that record.                                                                                                    |
| 404        | Not Found -- Resource not found.                                                                                                                      |
| 422        | Not processed – We're not able to process your request. Validate your parameters.                                                                     |
| 429        | Rate limit exceeded – You're being [throttled](https://developers.Velocityln.ai/#throttling) for exceeding our rate limit.                |
| 500        | Server error – We're having a problem with our server. Give us a few minutes and try again, or check [our status page](https://status.Velocityln.ai/) |

## Velocity Lean Change Log

The timestamps below are Eastern Time.

| Date                          | Description                                                                                                                       |
|-------------------------------| --------------------------------------------------------------------------------------------------------------------------------- |
                                                        |
