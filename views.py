from datetime import date

from components.models import Engine
from components.decorators import AppRoute
from origin.templator import render

site = Engine()
routes = {}

class NotFoud404:
    def __call__(self, request):
        return "404 WHAT", "404 PAGE Not Found"

@AppRoute(routes=routes, url='/')
class Index:
    def __call__(self):
        return "200 OK", render("index.html", object_list=site.categories)

@AppRoute(routes=routes, url='/about/')
class About:
    def __call__(self):
        return "200 OK", render("about.html", data=date.today())

@AppRoute(routes=routes, url='/contacts/')
class Contacts:
    def __call__(self):
        return "200 OK", render("contacts.html", data=date.today())

@AppRoute(routes=routes, url='/study_programs/')
class StudyPrograms:
    def __call__(self, request):
        return "200 OK", render("study-programs.html", data=date.today())

# Класс-контроллер - Страница "Список курсов"
@AppRoute(routes=routes, url='/courses_list/')
class CoursesList:
    def __call__(self, request):

        try:
            category = site.find_category_by_id(
                int(request["request_params"]["id"])
            )
            return "200 OK", render(
                "course_list.html",
                objects_list=category.courses,
                name=category.name,
                id=category.id,
            )
        except KeyError:
            return "200 OK", "No courses have been added yet"


# Класс-контроллер - Страница "Создать курс"
@AppRoute(routes=routes, url='/create_course/')
class CreateCourse:
    category_id = -1

    def __call__(self, request):
        if request["method"] == "POST":

            data = request["data"]

            name = data["name"]
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course("record", name, category)
                site.courses.append(course)

            return "200 OK", render(
                "course_list.html",
                objects_list=category.courses,
                name=category.name,
                id=category.id,
            )

        else:
            try:
                self.category_id = int(request["request_params"]["id"])
                print(f"ахх {request}")
                category = site.find_category_by_id(int(self.category_id))

                return "200 OK", render(
                    "create_course.html", name=category.name, id=category.id
                )
            except KeyError:
                return "200 OK", "No categories have been added yet"


# Класс-контроллер - Страница "Создать категорию"
@AppRoute(routes=routes, url='/create_category/')
class CreateCategory:
    def __call__(self, request):

        if request["method"] == "POST":

            print(request)
            data = request["data"]

            name = data["name"]
            name = site.decode_value(name)

            category_id = data.get("category_id")

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return "200 OK", render("index.html", objects_list=site.categories)
        else:
            categories = site.categories
            return "200 OK", render(
                "create_category.html", categories=categories
            )


# Класс-контроллер - Страница "Список категорий"
@AppRoute(routes=routes, url='/category_list/')
class CategoryList:
    def __call__(self, request):
        return "200 OK", render(
            "category_list.html", objects_list=site.categories
        )
