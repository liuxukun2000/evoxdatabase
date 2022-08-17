# evoxdatabase

## Usage

Download `db.sqlite3` from Google Drive: 

Unzip it into this folder.


### Example 1 (filter)
```python
>>> import init
>>> init.init()
>>> from nasbench101.models import NASBench101Result
>>> NASBench101Result.objects.filter(flops__gt=10000) # flops > 10000
>>> NASBench101Result.objects.filter(flops__lt=10000) # flops < 10000
>>> NASBench101Result.objects.filter(flops__lt=10000, params__gt=1) # flops < 10000 and params > 1
```

### Example 2 (update)
```python
>>> import init
>>> init.init()
>>> from nasbench101.models import NASBench101Result
>>> x = NASBench101Result.objects.filter(flops__gt=10000)[: 10] # get first 10 results
>>> x = x[0]
>>> x.flops = 100
>>> x.save()
```

### Example 3 (Sample)
```python
>>> import init
>>> init.init()
>>> from nasbench101.models import NASBench101Result
>>> NASBench101Result.objects.filter(index__lt=1000).order_by('?')[: 10] # Randomely sample 10 results
```

### Webpage
```bash
python manage.py runserver 0.0.0.0:8000
# usage: python manage.py runserver <IP>:<Port>
```
This will run a webserver on your computer(port: 8000)

Open http://localhost:8000/admin/

Login with:

Username: `test`

Password: `123321`

## Learn more about database, please visit https://docs.djangoproject.com/en/4.1/

## Acknowledgement

Codes are developed upon: [NAS-Bench-101](https://github.com/google-research/nasbench)
, [NAS-Bench-201](https://github.com/D-X-Y/NAS-Bench-201), [NAS-Bench-301](https://github.com/automl/nasbench301)
, [NATS-Bench](https://xuanyidong.com/assets/projects/NATS-Bench)
, [Once for All](https://github.com/mit-han-lab/once-for-all)
, [Django](https://www.djangoproject.com/)