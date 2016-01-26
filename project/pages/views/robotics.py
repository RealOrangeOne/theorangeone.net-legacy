from project.common.views import CustomTemplate


class IndexView(CustomTemplate):
    template_name = 'robotics/index.html'


# 2015
class Index2015View(CustomTemplate):
    template_name = 'robotics/2015-index.html'


class Robot2015View(CustomTemplate):
    template_name = 'robotics/2015-robot.html'


# 2014
class Index2014View(CustomTemplate):
    template_name = 'robotics/2014-index.html'
