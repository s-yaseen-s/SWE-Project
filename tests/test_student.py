from unittest.mock import MagicMock, patch

@patch("srs.controllers.student_controller.studentRepo")
def test_student_view_grades(mock_repo_class, client):
   
    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance
  
    mock_instance.get_grades.return_value = [
        {'course': 'CSAI203', 'grade': 'A'},
        {'course': 'MATH101', 'grade': 'B'}
    ]

   
    with client.session_transaction() as sess:
        sess['userID'] = 202401389
 
    response = client.get("/view_grades")

    
    assert response.status_code == 200

@patch("srs.controllers.student_controller.studentRepo")
def test_student_register_course_success(mock_repo_class, client):

    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance

    mock_instance.RegisterCourse.return_value = None 

    with client.session_transaction() as sess:
        sess['userID'] = 202401389

    response = client.post("/register_course", data={
        "course_id": "CSAI203"
    })

    assert response.status_code == 200