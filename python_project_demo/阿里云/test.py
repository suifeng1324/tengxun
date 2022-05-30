"""
@Author :       yangleiw
@File   :       .py
@Time   :       2022年05月22日 22:52
@Desc   :
"""

# if __name__ == "__main__":
#    pass


str={"sid":"1ff8983da7b9eea22fddd7db7100174a83d1e6d9d4064977dabe1986add27eb1513f5610","prism_version":"1.0.9","prism_wnum":5,"prism_wordsInfo":[{"word":"■1、","pos":[{"x":15,"y":14},{"x":49,"y":14},{"x":49,"y":28},{"x":15,"y":28}],"direction":0,"angle":-90,"x":24,"y":3,"width":14,"height":35},{"word":"+","pos":[{"x":59,"y":15},{"x":76,"y":15},{"x":76,"y":29},{"x":59,"y":29}],"direction":0,"angle":-90,"x":60,"y":13,"width":14,"height":18},{"word":"1有没有做过云项目+","pos":[{"x":28,"y":44},{"x":208,"y":44},{"x":208,"y":61},{"x":28,"y":61}],"direction":0,"angle":-90,"x":109,"y":-38,"width":17,"height":181},{"word":"2对华为自己本身的云设备了解多少(waf等) +","pos":[{"x":26,"y":69},{"x":433,"y":69},{"x":433,"y":86},{"x":26,"y":86}],"direction":0,"angle":-90,"x":220,"y":-126,"width":17,"height":408},{"word":"3有没有做过渗透测试","pos":[{"x":26,"y":94},{"x":225,"y":94},{"x":225,"y":111},{"x":26,"y":111}],"direction":0,"angle":-90,"x":116,"y":2,"width":17,"height":200}],"height":126,"width":712,"orgHeight":126,"orgWidth":712,"content":"■1、 + 1有没有做过云项目+ 2对华为自己本身的云设备了解多少(waf等) + 3有没有做过渗透测试 "}

for word in str["prism_wordsInfo"]:
    print(word["word"])