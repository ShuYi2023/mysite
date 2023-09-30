

# Markdown格式入门

一个'#'创建的是1级标题。

## 二级标题和要点

* 用'*'号可以创建bullet point.
* 两个'#'可以创建2级标题.
* 用'>'可以创建引用.

> 这里是引用.

高亮和填空, ==这里是前后4个等号包裹的内容==, 

* 要插入图片, 可以把图片链接放到这里.

![image.png|300](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230901143418.png)


















用反引号可以代码显示代码.

```bash
git clone https://github.com/jaymody/picoGPT
cd picoGPT
```

## 创建和激活虚拟环境

* 电脑中Anaconda要装好, 然后用conda创建好虚拟环境

    用'*'号可以创建bullet point.

```bash
conda create -n gpt_env python=3.9
conda activate gpt_env
pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
```



