#  福州商圈测评 

[这里有在线Demo](http://fuckse.rtxux.xyz/)

## 目录结构

- `data` ：数据目录，存放爬取和处理后的数据，以及聚类工具
- `frontend`：前端，需要使用vue-cli构建
- `server`：后端，需要Flask
- `spider`：爬虫，需要还原`environment.yml`

## 使用说明

### 爬虫

还原`environment.yml`应该就可以用，可能需要配一下代理池

### 后端

还原`environment.yml`就可以使用，其实只安装`flask`和`flask-cors`也行

运行`app.py`即可

### 前端

构建需要以下组件：

- Node.js
- Yarn
- `@vue-cli`
- 一个可用的高德地图的Key

首先需要填入高德Key，在`frontend/src/utils/AMap.js`

进入`frontend`目录后，依次运行`yarn install`和`yarn run build`即可在`dist`目录获得分发包，或运行`yarn run serve`即可启动开发服务器