job平台command界面


example.py   示例

JOB状态：run_status          
	0 创建  、1等待  、2运行  、3完成


	0 创建		创建、且无运行时间（默认值）

	1 创建就绪	创建后，等待调度时间到来
	2 创建等待	创建后，等待依赖完成

	3 运行		运行中

	4 调度就绪	运行后，等待再次调度
	5 调度等待	运行后，等待依赖完成后再次调度

	6 完成		所有调度完成

JOB状态：run_status
	创建		创建、且无运行时间（默认值）      0
	等待  	创建后,允许调度,等待调度时间到来  1
	运行		运行中                        2
	完成		所有调度完成                   3
