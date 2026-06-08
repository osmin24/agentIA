from session_manager import SessionManager, Message

def test_create_session():
    sm = SessionManager()
    session_id = sm.create_session()
    assert session_id is not None
    assert session_id in sm.sessions
    assert sm.sessions[session_id] == []

def test_add_exchange_and_ordering():
    sm = SessionManager()
    session_id = sm.create_session()
    sm.add_exchange(session_id, "Hola", "Hola! Soy el asistente.")
    
    assert len(sm.sessions[session_id]) == 2
    assert sm.sessions[session_id][0].role == "user"
    assert sm.sessions[session_id][0].content == "Hola"
    assert sm.sessions[session_id][1].role == "assistant"
    assert sm.sessions[session_id][1].content == "Hola! Soy el asistente."

def test_access_non_existent_session():
    sm = SessionManager()
    history = sm.get_conversation_history("session_999")
    assert history is None
