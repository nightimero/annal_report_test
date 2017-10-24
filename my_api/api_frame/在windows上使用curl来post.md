### 在windows上使用curl来post
- **linux上的格式**
```
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://192.168.1.91:5000/todo/api/v1.0/tasks
```
- **windows上的格式**

`方法是使用双引号括起逸出的值和标题参数值 `
```
curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Read a book again"""}" http://192.168.1.91:5000/todo/api/v1.0/tasks
curl -i -H "Content-Type: application/json" -X POST -d "{\"title\":\"Read a book again\"}" http://192.168.1.91:5000/todo/api/v1.0/tasks
```
