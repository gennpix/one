## 需求
1. 四层+七层的负载均衡
2. 一旦发现故障服务器，则将其从负载均衡组中摘除
3. 支持session保持
4. 企业级的负载均衡，高效的方案

## 硬件昂贵的商用的负载均衡器
- NetScaler
- F5
- Radware
- Array等
## 商业负载均衡软件
- PCL
## 免费的开源负载均衡软件
1. LVS
    建议在简单的LINUX应用中使用LVS，复杂的应用，或者重要的应用，还是应该使用专业的负载均衡软件。
    **优点:** 
     1、开源，免费 
     2、在网上能找到一些相关技术资源 
     3、具有软件负载均衡的一些优点  
    **缺点：** 
     1、具有开源产品常有的缺点，最核心的就是没有可靠的支持服务，没有人对其结果负责 
     2、功能比较简单，支持复杂应用的负载均衡能力较差，如算法较少等。 
     3、开启隧道方式需重编译内核 
     4、配置复杂 
     5、只支持LINUX，如果应用还包括WINDOWS、SOLIRIS等就不行了

2. DR
3. Keepalived
4. Nginx
5. HAProxy

## 选择的方案
1. LVS/DR+Keepalived
    优点：
    缺点：实施复杂
2. Nginx/HAProxy+Keepalived
    优点：简单
    缺点：
## 相关技术
- 基于DNS的负载均衡
  优点：实现简单、实施容易、成本低、适用于大多数TCP/IP应用；
  缺点：
    1、 负载分配不均匀，DNS服务器将Http请求平均地分配到后台的Web服务器上，而不考虑每个Web服务器当前的负载情况；如果后台的Web服务器的配置和处理能力不同，最慢的Web服务器将成为系统的瓶颈，处理能力强的服务器不能充分发挥作用；
    2、可靠性低，如果后台的某台Web服务器出现故障，DNS服务器仍然会把DNS请求分配到这台故障服务器上，导致不能响应客户端。
    3、变更生效时间长，如果更改NDS有可能造成相当一部分客户不能享受Web服务，并且由于DNS缓存的原因，所造成的后果要持续相当长一段时间(一般DNS的刷新周期约为24小时)。
- 基于四层交换技术的负载均衡
  优点：性能高、支持各种网络协议
  缺点：对网络依赖较大，负载智能化方面没有7层负载好（比如不支持对url个性化负载），F5硬件性能很高但成本也高需要人民币几十万，对于小公司就望而却步了。
- 基于七层交换技术的负载均衡
  具有代表意义的产品：nginx（软件）、apache（软件）
  优点：对网络依赖少，负载智能方案多（比如可根据不同的url进行负载）
  缺点：网络协议有限，nginx和apache支持http负载，性能没有4层负载高

- 负载均衡软件实现方式之一 - URL重定向方式

- 使用四层+七层负载结合方案
  四层负载使用lvs软件或F5硬件实现。
  七层负载使用nginx实现。



## 根据发展趋势选择负载均衡技术
现在网站发展的趋势对网络负载均衡的使用是随着网站规模的提升根据不同的阶段来使用不同的技术：
- 第一阶段：利用Nginx或者HAProxy进行单点的负载均衡，这一阶段服务器规模刚脱离开单服务器、单数据库的模式，需要一定的负载均衡，但是仍然规模较小没有专业的维护团队来进行维护，也没有需要进行大规模的网站部署。这样利用Nginx或者HAproxy就是第一选择，此时这些东西上手快，配置容易，在七层之上利用HTTP协议就可以。这时是第一选择。
- 第二阶段：随着网络服务进一步扩大，这时单点的Nginx已经不能满足，这时使用LVS或者商用F5就是首要选择，Nginx此时就作为LVS或者 F5的节点来使用，具体LVS或者F5的是选择是根据公司规模，人才以及资金能力来选择的，这里也不做详谈，但是一般来说这阶段相关人才跟不上业务的提 升，所以购买商业负载均衡已经成为了必经之路。
- 第三阶段：这时网络服务已经成为主流产品，此时随着公司知名度也进一步扩展，相关人才的能力以及数量也随之提升，这时无论从开发适合自身产品的定制，以及降低成本来讲开源的LVS，已经成为首选，这时LVS会成为主流。
  
## 灰度发布（金丝雀发布）
### 简单实现方案
2个不同的deployment，同一个service，通过修改Replicas控制比例
### 基于用户特性的灰度
待研究！

## 蓝绿发布
在k8s集群中部署两套服务，经过测试后的蓝，如何上线成绿以及前绿的下线？
待研究！

## 参考
### 负载均衡
1. https://blog.csdn.net/qq_41455420/article/details/79846199
2. https://www.jianshu.com/p/c322701da246
## 灰度发布
1. https://cloud.tencent.com/developer/article/1590808