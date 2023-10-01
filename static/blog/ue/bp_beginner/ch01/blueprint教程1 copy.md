Max的课程对设备有各种要求. 所以,

- 建议准备一个 Pad, 用Pad看教程, 用Mac或者PC实际操作.    
- 英文不太好的同学, 不建议学习本课程.

## 1.项目最终结果演示
(在电脑上演示, 或者贴一个视频)

## 2.安装和打开Unreal Engine 5

- √安装和打开Unreal Engine 5; 创建一个名为`LearnBP`的项目。
    * √本教程在呈现内容的时候, 通常分两部分: 文字说明 + 图片。图片常常不止只有一个, 所以要看全部的图片哦。

![image.png|750](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924084346.png)

![image.png|550](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924084433.png)

- √Play一下. Esc退出Play。

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924084510.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924084531.png)


## 3.创建一个Blueprint

- √打开content drawer.
  
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924084906.png)

- √添加一个文件夹, 取名Blueprints. 

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924084941.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924084948.png)

* 理解一下UE中文件夹的层级。在UE中, 下图是项目的根目录, Content目录以及项目的.uproject文件。 #flashcard
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924110608.png)
<!--ID: 1695545559562-->

### 在文件夹中添加一个 Blueprint

- √右键点击 Blueprints 文件夹, 然后按照下图选择 `Add/Import Content`, 再选择 `Blueprint Class`.

![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924090953.png)

- √选择 Actor作为这个 Blueprint的`父类`.

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091105.png)

- √把新建的 Blueprint 改名为 `BP_Test`.

![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091134.png)

- √在文件夹中双击 BP_Test 打开这个蓝图进行编辑。
    
- √把 BP_Test 标签页(tab)拖到ThirdPersonMap旁边。
    
![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091230.png)

![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091244.png)

### 给蓝图添加一个球体.

我们可以把蓝图理解为{ 蓝图 = 形状 + 逻辑 = 外形 + 思想 }。外形有Shpere等样子, 逻辑用`Event Graph`管理。
<!--ID: 1695545559533-->

- √在 Components 下面选中BP_Test; 点击Add, 输入sphe, 从提示中选择Sphere; 别选成 Sphere Collision 了.
    
![image.png|250](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091315.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091343.png)

- 添加 Sphere 之后, Components 下面是这样。

![image.png|550](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091427.png)

- √compile, save.
    
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091452.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091501.png)

- 切换到`ThirdPersonMap`; 把BP拖到`ThirdPersonMap`中.

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091555.png)

## 4.修改BP

- √设置BP的大小。点击 `BP_Test` 标签, 回到BP_Test蓝图界面; 选中Sphere; 找到Details标签; 把Scale的(x, y, z)的值都设置为0.5。这样能够把球体变小。

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091623.png)

- √在 Details 中找到 Simulate Physics(模拟物理), 勾选.
    
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924091643.png)

- √compile, save
    
- √回到地图, Play, 这时的球应该可以踢了。
## 5.Event Graph

- √找到 `BP_Test` 的`Event Graph` 标签, 点击, 切换到Event Graph画面. (在**画布**的空白处按住鼠标右键不放, 可以拖动整个画布)
    
![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924112732.png)

- √删除事件 `Event BeginPlay`. (不用担心, 以后还可以添加上去。另外, Ctrl + Z 可以撤销删).
    
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924113008.png)

- 添加事件的方法: 右键点击空白处, 搜索要添加的事件node. 也可以移动node.
    
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924113155.png)

## 6.`BeginPlay`事件研究
    
- 对于`BP_Test`这个蓝图, 一旦我们开始游戏, 就会执行这个`Event BeginPlay`事件. 对于新出生(spawn)的actor, 也会在spawn时候触发这个事件.
    
### **`Print String`**, 下面的任务是在游戏界面上打印"您好!".

- 参考下面的图示, 从`Event BeginPlay`的引脚拖出一根线;
    
    - 搜索`Print String`动作(action)并选择;
        
    - 把 `In String` 参数设置为`您好!`;
        
    - compile save ;
        
    - 切换到Map中去执行.
        
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924113515.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924113541.png)

> In String要和`Print String`连起来看, 所以是Print <变量> In String. 这个函数把"您好!"变成String类型之后, 再打印。

- √执行时能够看到
    
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924113908.png)

* √在地图中放置多个BP_Test, 会多次打印`您好!`。

- √在Map的`Outliner`中找到添加的BP_Test, 按delete键删除它们. (由于内容很多, 建议多用Search功能)
    
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924114043.png)

### Get World Scale 获得世界的大小

- 在Details中查看 Sphere 的 scale;
    
    - √把Sphere拖到编辑器中; 从引脚中引出`Get World Scale`;
        
    - √连接 Return Value 和 In String;
        
    - √展开`Development Only`, 将持续时间(Duration)设置为5.0秒.
        
![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924114900.png)

![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924114929.png)

- √compile save. 到地图中Play. 这是一种很好的调试方法。

![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924115226.png)

### Get World Scale的解释如下。
* 在`Get World Scale`中需要填入一个Target变量, 这个变量由Sphere填入, 整个函数的意思是{获得 Sphere 在 World 中的 Scale}。我们看函数的方法通常是: 函数的名字, 名字通常就表明的这个函数能实现什么功能, 然后看执行函数需要什么变量。然后, 给变量赋值。另外要注意, 这个 `Event Graph` 是属于 `BP_Test` 的.
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924115057.png)
<!--ID: 1695545559556-->

## 7.更改BP的材质(Material)

* 更改蓝图中某个物体或者形状的材质
    - √选中`Component`中的`Sphere`,
    - √在Details中导航到Sphere的材质(Material);
    - √更改其材质为`M_Brick_Clay_New`;
    - √在Map中查看更改效果; 以后可以把材质再改回BasicShapeMaterial。

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924115828.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924115835.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924115844.png)

### Set Material

- √回到蓝图的Event Graph, 我们来用脚本改变材质.
![image.png|550](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924120340.png)

- √接上图, 在Print String之后, `Set Material` 
    
![image.png|550](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924120426.png)

- √Play, 测试一下. 可见`Set Material`也是一个高层级的静态函数, 或者说全局函数。
    

## 8.Construction Script
    
Construction Script相当于构造函数。在 `construction script` 中也可以更改Sphere的材质。 `construction script`类似构造函数. 可以预先做出蓝图的实例.

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924120700.png)

- √在Even Graph页面框选Blueprint代码; ctrl+c复制; 拷贝到Construction Script的画布上.
    
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924120808.png)

![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924120819.png)

- √依照下图改造一下这个BP; Save; Compile.
    
![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924120938.png)

- √观察. 发现不用开始游戏, 在编辑器中球就变成金黄色的了。但是看不到Location的三维坐标的显示.
    
- √打开Output Log, 拖动Sphere的时候, 可以观察到其坐标的改变.
    
![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924121102.png)

* √Construction Script的作用是, 可以预修改Asset的一些属性, 而不是在游戏开始后修改。一个用途是: 让金色的球在空间随机分布; 或者让草木在庭院中随机分布。

## 9.Event Tick
    
- Tick事件每帧都会执行. 计算机每秒钟一般能运行30到300帧, 这就是帧率(FPS, Frame Per Second)。执行Tick事件需要时间, 因此为了保证游戏的流畅度, 最好只是在必要的时候才使用Tick。
    
- √查看游戏的FPS(Frame Per Second).
    
![image.png|250](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924121259.png)

- √Play, 可以看到游戏的帧率.
    
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924121400.png)

## 10.Text Color -- 显示有色彩的文本.
    
### Random Array Item

* √按住 Text Color 前面的引脚, 往`左边`拖动.

![image.png|350](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924121519.png)

- √选择`Random Array Item`.

![image.png|350](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924121635.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924121643.png)

### Make Array

* √Make Array
![image.png|350](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924121934.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924121941.png)

- 设置颜色
    - √点击下图所示的方框,
    - √设置颜色的Value,
    - √设置饱和度(Saturation).

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924122228.png)

- √点击Add Pin, 再增加两个数组元素[1]和[]2; 并设置好颜色和饱和度.
- √连上`Event Tick`。Compile, Save。Play。

![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924122323.png)

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924122331.png)


- 使用cmd强制把FPS设为5. 可以看到输出Hello的速度明显慢了很多。而且游戏的流畅度感觉也差了很多.
    
![image.png|550](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924122615.png)

- 将FPS设为0, 恢复到正常状态。
    
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924122636.png)

## (Optional)

### 用5.3版本打开5.1版本, 为了节省空间, 可以conversion #flashcard 
![image.png|650](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230924105416.png)
<!--ID: 1695545559567-->

