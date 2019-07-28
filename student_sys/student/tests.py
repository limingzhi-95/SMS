from django.test import TestCase
from django.test.client import Client

from student_sys.student.models import Student


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name='test',
            sex=1,
            email='123@123.com',
            profession='programmer',
            qq='2333',
            phone='12345'
        )

    def tearDown(self):
        pass

    def test_sex_show(self):
        self.assertEqual(self.student.sex_show, '男', msg='性别字段展示不对')

    def test_filter(self):
        name = 'programmer'
        students = Student.objects.filter(Student.name == name)
        self.assertEqual(students.count(), 1, '姓名为{}的数据只应该存在一条'.format(name))


class ViewIndexTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.path = '/'

    def test_get_index(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200, msg='status code must be 200!')

    def test_post_student(self):
        data = dict(
            name='test_post',
            sex=2,
            email='123@123.com',
            profession='programmer_post',
            qq='2333',
            phone='12345'
        )
        response = self.client.post(self.path, data=data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = self.client.get(self.path)
        self.assertTrue(b'test_post' in response.content, 'response content must contain `test_post`')
