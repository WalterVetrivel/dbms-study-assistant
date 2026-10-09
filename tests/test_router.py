from dbms_bot.agent import route_by_keyword


def test_quiz_me_routes_to_quiz():
    assert route_by_keyword("quiz me on joins") == "generate_quiz"


def test_explain_routes_to_explain():
    assert route_by_keyword("Explain BCNF simply") == "explain_topic"


def test_default_is_answer():
    assert route_by_keyword("What is a candidate key?") == "answer_question"
