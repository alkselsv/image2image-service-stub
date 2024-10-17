# image2image-service-stub

## Запуск

```
docker build -t image2image-service-stub .

docker run -d -p 8000:8000 image2image-service-stub
```

## Тестирование эндпойнтов

Для тестирование используется утилита [httpie](https://httpie.io).

```
http -f POST http://localhost:8000/segment file@test_image.jpg -o segment_result.jpg

http -f POST http://localhost:8000/transform file@test_image.jpg -o transform_result.jpg
```
