from .supabase_client import supabase

def add_document(tittel, innhold):
    data = {"tittel": tittel, "innhold": innhold}
    return supabase.table("kontekst.dokumenter").insert(data).execute()