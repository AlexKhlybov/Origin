from views import (
    About,
    CategoryList,
    Contacts,
    CoursesList,
    CreateCategory,
    CreateCourse,
    Index,
    StudyPrograms,
)

routes = {
    "/": Index(),
    "/about/": About(),
    "/contacts/": Contacts(),
    "/study_programs/": StudyPrograms(),
    "/courses-list/": CoursesList(),
    "/create-course/": CreateCourse(),
    "/create-category/": CreateCategory(),
    "/category-list/": CategoryList(),
}
