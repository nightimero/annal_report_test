### 在linux中
#### 总结： 不同的脚本类型需要不同的excecute窗口。
第一个shell中，在Excecute shell中执行命令：
```python
#!/usr/bin/env python
print 'hello world'
```

在第二个shell中，在Excecute shell中执行命令：
```shell
echo 'hello world'
```



`执行结果：

Started by user 干老师

Building in workspace /var/lib/jenkins/workspace/test_chen

[test_chen] $ /bin/sh -xe /tmp/jenkins24447195345476408.sh

\+ echo 'hello world'

hello world

[test_chen] $ /usr/bin/env python /tmp/jenkins8812013487223493996.sh

hello tester

Finished: SUCCESS