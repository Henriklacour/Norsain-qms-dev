from src.qms.supabase_client import supabase

def test_connection():
    assert supabase is not None, "Supabase-tilkobling feilet"