from project.common.views import CustomTemplate, MarkdownView


class IndexView(CustomTemplate):
    template_name = 'robotics/index.html'
    html_title = 'Student Robotics'


# 2015
class Index2015View(CustomTemplate):
    template_name = 'robotics/2015-index.html'
    html_title = 'Student Robotics 2015'


class Robot2015View(CustomTemplate):
    template_name = 'robotics/2015-robot.html'
    html_title = 'The Robot | SR2015'


class Code2015View(MarkdownView):
    markdown = 'robotics/2015-code.md'


# 2014
class Index2014View(CustomTemplate):
    template_name = 'robotics/2014-index.html'
    html_title = 'Student Robotics 2014'
