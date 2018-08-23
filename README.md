Curly
=====


```
http http://localhost:5000/schema/
```

```
echo '{"name": "tst", "rating": 1, "in_stock": true, "size":"m"}' | http post localhost:5000/data
echo '{"name": "tst", "rating": 1, "in_stock": true, "size":"large"}' | http post localhost:5000/data
```