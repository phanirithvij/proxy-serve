# Http Server Python

A http-server made using socket programming in python.

## Run

```shell
python3 server.py
```

Then configure the system proxy settings pointing to the `localhost, 5000`

Visit these for example

- [http://csg.iiit.ac.in/](http://csg.iiit.ac.in/)
- [http://dsac.iiit.ac.in/](http://dsac.iiit.ac.in/)
- [http://lsi.iiit.ac.in/](http://lsi.iiit.ac.in/) (Black listed) (10.4.16.178)

Implemented:
- black listing in CIDR format
- server side caching within 5min and max memory of 3 cached requests
- threaded proxy server
- authentication

### Authentication

Change username and password

```shell
curl --request GET -u username:password --proxy 127.0.0.1:5000 http://lsi.iiit.ac.in
```

<!-- ## Browser side testing -->

<!-- ### For a form
```javascript
var data = new FormData();
data.append('user', 'person');
data.append('pwd', 'password');
data.append('organization', 'place');
data.append('requiredkey', 'key');

var xhr = new XMLHttpRequest();
xhr.open('POST', '/', true);
xhr.onload = function () {
    // do something to response
    console.log(this.responseText);
};
xhr.send(data);

```

### For a post json
```javascript
fetch(
    "/",
    {
        method:"POST",
        body:JSON.stringify({
            fakk:{f:{a:[{x:'a'}]}}
        })
    })
    .then(s=>s.json())
    .then(s=>console.log(s));

``` -->
