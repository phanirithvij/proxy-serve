# Http Server Python

A http-server made using socket programming in python.

## Run

```shell
python3 server.py
```

## to run the cache module

```shell
python3 cacher.py
```

Then configure the system proxy settings pointing to the `localhost, 5000`

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
