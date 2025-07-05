# Here is the plan:
# 1. Get list of all tables in db1
# 2. Begin copying data from db1 to db2
# 3. Start with the easy ones, exact same tables/columns.
from tqdm import tqdm

def migrate(source_db, new_db):
    cursor_source = source_db.cursor(dictionary=True)
    cursor_target = new_db.cursor(dictionary=True)

    # ==== Commented out below to speed up testing, but should be working. ====
    m_ahbot_category(cursor_source, cursor_target, new_db)
    m_ahbot_history(cursor_source, cursor_target, new_db)
    m_ahbot_price(cursor_source, cursor_target, new_db)
    m_ai_playerbot_names(cursor_source, cursor_target, new_db)
    m_ai_playerbot_random_bots(cursor_source, cursor_target, new_db)
    m_auction(cursor_source, cursor_target, new_db)
    m_bugreport(cursor_source, cursor_target, new_db)
    m_character_action(cursor_source, cursor_target, new_db)
    m_character_aura(cursor_source, cursor_target, new_db)
    m_character_battleground_data(cursor_source, cursor_target, new_db)
    m_character_gifts(cursor_source, cursor_target, new_db)
    m_character_homebind(cursor_source, cursor_target, new_db)
    m_character_honor_cp(cursor_source, cursor_target, new_db) # ==== Needs work, read function comments.
    m_character_instance(cursor_source, cursor_target, new_db)
    m_character_inventory(cursor_source, cursor_target, new_db)
    m_character_pet(cursor_source, cursor_target, new_db)
    m_character_queststatus(cursor_source, cursor_target, new_db)
    m_character_reputation(cursor_source, cursor_target, new_db)
    m_character_skills(cursor_source, cursor_target, new_db)
    m_character_social(cursor_source, cursor_target, new_db)
    m_character_spell(cursor_source, cursor_target, new_db)
    m_character_spell_cooldown(cursor_source, cursor_target, new_db)
    m_character_stats(cursor_source, cursor_target, new_db) # ==== Needs work, read function comments.
    m_character_ticket(cursor_source, cursor_target, new_db)
    m_character_tutorial(cursor_source, cursor_target, new_db)
    m_character_whispers(cursor_source, cursor_target, new_db)
    m_characters(cursor_source, cursor_target, new_db) # ==== Needs work, read function comments.
    m_corpse(cursor_source, cursor_target, new_db)
    m_creature_respawn(cursor_source, cursor_target, new_db)
    m_game_event_status(cursor_source, cursor_target, new_db)
    m_gameobject_respawn(cursor_source, cursor_target, new_db)
    m_group_instance(cursor_source, cursor_target, new_db)
    m_group_member(cursor_source, cursor_target, new_db)
    m_groups(cursor_source, cursor_target, new_db)
    m_guild(cursor_source, cursor_target, new_db)
    m_guild_eventlog(cursor_source, cursor_target, new_db)
    m_guild_member(cursor_source, cursor_target, new_db)
    m_guild_rank(cursor_source, cursor_target, new_db)
    m_instance(cursor_source, cursor_target, new_db)
    m_instance_reset(cursor_source, cursor_target, new_db)
    m_item_instance(cursor_source, cursor_target, new_db)
    m_item_loot(cursor_source, cursor_target, new_db)
    m_mail(cursor_source, cursor_target, new_db)
    m_mail_items(cursor_source, cursor_target, new_db)
    m_pet_aura(cursor_source, cursor_target, new_db)
    m_pet_spell(cursor_source, cursor_target, new_db)
    m_pet_spell_cooldown(cursor_source, cursor_target, new_db)
    m_petition(cursor_source, cursor_target, new_db)
    m_petition_sign(cursor_source, cursor_target, new_db)
    m_pvpstats_battlegrounds(cursor_source, cursor_target, new_db)
    m_pvpstats_players(cursor_source, cursor_target, new_db)
    m_quest_tracker(cursor_source, cursor_target, new_db)
    m_saved_variables(cursor_source, cursor_target, new_db)
    m_warden_action(cursor_source, cursor_target, new_db)
    m_world(cursor_source, cursor_target, new_db)


def m_ahbot_category(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'ahbot_category' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "ahbot_category"
    columns_to_copy = ["id", "category", "multiplier", "max_auction_count", "expire_time"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_ahbot_history(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'ahbot_history' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "ahbot_history"
    columns_to_copy = ["id", "buytime", "item", "bid", "buyout", "won", "category", "auction_house"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_ahbot_price(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'ahbot_price' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "ahbot_price"
    columns_to_copy = ['"id"', '"item"', '"price"', '"auction_house"']

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_ai_playerbot_names(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'ai_playerbot_names' table in the source database to the target database.
    MaNGOS One dropped race, class, purpose, priority, and in_use.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "ai_playerbot_names"
    columns_to_copy = ["name_id", "name", "gender"]

    delete_query = f"DELETE FROM {table_name}"
    cursor_target.execute(delete_query)
    new_db.commit()

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_ai_playerbot_random_bots(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'ai_playerbot_random_bots' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "ai_playerbot_random_bots"
    columns_to_copy = ["id", "owner", "bot", "time", "validIn", "event", "value", "data"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_auction(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'auction' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "auction"
    columns_to_copy = ["id", "houseid", "itemguid", "item_template", "item_count", "item_randompropertyid", "itemowner", "buyoutprice", "time", "buyguid", "lastbid", "startbid", "deposit"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_bugreport(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'bugreport' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "bugreport"
    columns_to_copy = ["id", "type", "content"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_action(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_action' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_action"
    columns_to_copy = ["guid", "button", "action", "type"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_aura(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_aura' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_aura"
    columns_to_copy = ["guid", "caster_guid", "item_guid", "spell", "stackcount", "remaincharges", "basepoints0", "basepoints1", "basepoints2", "periodictime0", "periodictime1", "periodictime2", "maxduration", "remaintime", "effIndexMask"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_battleground_data(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_battleground_data' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_battleground_data"
    columns_to_copy = ["guid", "instance_id", "team", "join_x", "join_y", "join_z", "join_o", "join_map"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_gifts(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_gifts' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_gifts"
    columns_to_copy = ["guid", "item_guid", "entry", "flags"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_homebind(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_homebind' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_homebind"
    columns_to_copy = ["guid", "map", "zone", "position_x", "position_y", "position_z"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_honor_cp(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_honor_cp' table in the source database to the target database.
    Table does not exist in MaNGOS One - need to find the destination for this data.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_honor_cp"
    # columns_to_copy = ["guid", "victim_type", "victim", "honor", "date", "type", "used"]

    # insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    # cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    # rows = cursor_source.fetchall()

    # progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    # for row in rows:
    #     values = [row[column] for column in columns_to_copy]
    #     cursor_target.execute(insert_query, values)
    #     new_db.commit()
    #     progress_bar.update(1)  # Update progress bar

    # # Close and clear progress bar
    # progress_bar.close()

def m_character_instance(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_instance' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_instance"
    columns_to_copy = ["guid", "instance", "permanent"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_inventory(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_inventory' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_inventory"
    columns_to_copy = ["guid", "bag", "slot", "item", "item_template"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_pet(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_pet' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_pet"
    columns_to_copy = ["id", "entry", "owner", "modelid", "CreatedBySpell", "PetType", "level", "exp", "Reactstate", "loyaltypoints", "loyalty", "trainpoint", "name", "renamed", "slot", "curhealth", "curmana", "curhappiness", "savetime", "resettalents_cost", "resettalents_time", "abdata", "teachspelldata"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_queststatus(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_queststatus' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_queststatus"
    columns_to_copy = ["guid", "quest", "status", "rewarded", "explored", "timer", "mobcount1", "mobcount2", "mobcount3", "mobcount4", "itemcount1", "itemcount2", "itemcount3", "itemcount4"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_reputation(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_reputation' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_reputation"
    columns_to_copy = ["guid", "faction", "standing", "flags"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_skills(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_skills' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_skills"
    columns_to_copy = ["guid", "skill", "value", "max"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_social(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_social' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_social"
    columns_to_copy = ["guid", "friend", "flags"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_spell(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_spell' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_spell"
    columns_to_copy = ["guid", "spell", "active", "disabled"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_spell_cooldown(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_spell_cooldown' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_spell_cooldown"
    columns_to_copy = ["guid", "spell", "item", "time"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_stats(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_stats' table in the source database to the target database.
    There are two new columns in MaNGOS One: spellCritPct and spellPower.
    Currently, this function does NOT write any data into these columns - will need to determine what the formulas are to determine these 2 values.
    Also, will need to assess whether any other formulas may need to be recalculated for the stats. Right now, this function only COPIES direct values.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_stats"
    columns_to_copy = ["guid", "maxhealth", "maxpower1", "maxpower2", "maxpower3", "maxpower4", "maxpower5", "maxpower6", "maxpower7", "strength", "agility", "stamina", "intellect", "spirit", "armor", "resHoly", "resFire", "resNature", "resFrost", "resShadow", "resArcane", "blockPct", "dodgePct", "parryPct", "critPct", "rangedCritPct", "attackPower", "rangedAttackPower"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_ticket(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_ticket' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_ticket"
    columns_to_copy = ["ticket_id", "guid", "ticket_text", "response_text", "ticket_lastchange", "resolved"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_tutorial(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_tutorial' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_tutorial"
    columns_to_copy = ["account", "tut0", "tut1", "tut2", "tut3", "tut4", "tut5", "tut6", "tut7"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_character_whispers(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'character_whispers' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "character_whispers"
    columns_to_copy = ["id", "to_guid", "from_guid", "message", "regarding_ticket_id", "sent_on"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_characters(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'characters' table in the source database to the target database.
    M0====
    honor_highest_rank
    honor_standing
    stored_honor_rating
    stored_dishonorable_kills
    stored_honorable_kills

    M1====
    arenaPoints
    totalHonorPoints
    yesterdayHonorPoints
    totalKills
    ysterdayKills

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "characters"
    columns_to_copy = ["guid", "account", "name", "race", "class", "gender", "level", "xp", "money", "playerBytes", "playerBytes2", "playerFlags", "position_x", "position_y", "position_z", "map", "orientation", "taximask", "online", "cinematic", "totaltime", "leveltime", "logout_time", "is_logout_resting", "rest_bonus", "resettalents_cost", "resettalents_time", "trans_x", "trans_y", "trans_z", "trans_o", "transguid", "extra_flags", "stable_slots", "at_login", "zone", "death_expire_time", "taxi_path", "watchedFaction", "drunk", "health", "power1", "power2", "power3", "power4", "power5", "exploredZones", "equipmentCache", "ammoId", "actionBars", "deleteInfos_Account", "deleteInfos_Name", "deleteDate"]


    # need to do special handling with: "honor_highest_rank", "honor_standing", "stored_honor_rating", "stored_dishonorable_kills", "stored_honorable_kills"


    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_corpse(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'corpse' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "corpse"
    columns_to_copy = ["guid", "player", "position_x", "position_y", "position_z", "orientation", "map", "time", "corpse_type", "instance"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_creature_respawn(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'creature_respawn' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "creature_respawn"
    columns_to_copy = ["guid", "respawntime", "instance"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_game_event_status(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'game_event_status' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "game_event_status"
    columns_to_copy = ["event"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_gameobject_respawn(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'gameobject_respawn' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "gameobject_respawn"
    columns_to_copy = ["guid", "respawntime", "instance"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()
    
def m_group_instance(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'group_instance' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "group_instance"
    columns_to_copy = ["leaderGuid", "instance", "permanent"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_group_member(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'group_member' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "group_member"
    columns_to_copy = ["groupId", "memberGuid", "assistant", "subgroup"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_groups(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'groups' table in the source database to the target database.
    MaNGOS One added difficulty - but shouldn't be necessary to fill in during migration.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "groups"
    columns_to_copy = ["groupId", "leaderGuid", "mainTank", "mainAssistant", "lootMethod", "looterGuid", "lootThreshold", "icon1", "icon2", "icon3", "icon4", "icon5", "icon6", "icon7", "icon8", "isRaid"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_guild(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'guild' table in the source database to the target database.
    MaNGOS One added BankMoney - but shouldn't be necessary to fill in during migration.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "guild"
    columns_to_copy = ["guildid", "name", "leaderguid", "EmblemStyle", "EmblemColor", "BorderStyle", "BorderColor", "BackgroundColor", "info", "motd", "createdate"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_guild_eventlog(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'guild_eventlog' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "guild_eventlog"
    columns_to_copy = ["guildid", "LogGuid", "EventType", "PlayerGuid1", "PlayerGuid2", "NewRank", "TimeStamp"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_guild_member(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'guild_member' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "guild_member"
    columns_to_copy = ["guildid", "guid", "rank", "pnote", "offnote"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_guild_rank(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'guild_rank' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "guild_rank"
    columns_to_copy = ["guildid", "rid", "rname", "rights"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_instance(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'instance' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "instance"
    columns_to_copy = ["id", "map", "resettime", "data"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_instance_reset(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'instance_reset' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "instance_reset"
    columns_to_copy = ["mapid", "resettime"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_item_instance(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'item_instance' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "item_instance"
    columns_to_copy = ["guid", "owner_guid", "data"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_item_loot(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'item_loot' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "item_loot"
    columns_to_copy = ["guid", "owner_guid", "itemid", "amount", "property"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_mail(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'mail' table in the source database to the target database.
    MangosOne dropped the body column and added the itemTextId column. Currently this is not resolved in the function below.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "mail"
    columns_to_copy = ["id", "messageType", "stationery", "mailTemplateId", "sender", "receiver", "subject", "has_items", "expire_time", "deliver_time", "money", "cod", "checked"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_mail_items(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'mail_items' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "mail_items"
    columns_to_copy = ["mail_id", "item_guid", "item_template", "receiver"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_pet_aura(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'pet_aura' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "pet_aura"
    columns_to_copy = ["guid", "caster_guid", "item_guid", "spell", "stackcount", "remaincharges", "basepoints0", "basepoints1", "basepoints2", "periodictime0", "periodictime1", "periodictime2", "maxduration", "remaintime", "effIndexMask"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_pet_spell(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'pet_spell' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "pet_spell"
    columns_to_copy = ["guid", "spell", "active"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_pet_spell_cooldown(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'pet_spell_cooldown' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "pet_spell_cooldown"
    columns_to_copy = ["guid", "spell", "time"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_petition(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'petition' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "petition"
    columns_to_copy = ["ownerguid", "petitionguid", "name"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_petition_sign(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'petition_sign' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "petition_sign"
    columns_to_copy = ["ownerguid", "petitionguid", "playerguid", "player_account"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_pvpstats_battlegrounds(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'pvpstats_battlegrounds' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "pvpstats_battlegrounds"
    columns_to_copy = ["id", "winner_team", "bracket_id", "type", "date"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_pvpstats_players(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'pvpstats_players' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "pvpstats_players"
    columns_to_copy = ["battleground_id", "character_guid", "score_killing_blows", "score_deaths", "score_honorable_kills", "score_bonus_honor", "score_damage_done", "score_healing_done", "attr_1", "attr_2", "attr_3", "attr_4", "attr_5"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_quest_tracker(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'quest_tracker' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "quest_tracker"
    columns_to_copy = ["id", "character_guid", "quest_accept_time", "quest_complete_time", "quest_abandon_time", "completed_by_gm", "core_hash", "core_revision"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_saved_variables(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'saved_variables' table in the source database to the target database.
    MaNGOS One dropped NextMaintenanceDate.


    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "saved_variables"
    columns_to_copy = ["cleaning_flags"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_warden_action(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'warden_action' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "warden_action"
    columns_to_copy = ["wardenid", "action"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()

def m_world(cursor_source, cursor_target, new_db):
    """
    Migrate data from the 'world' table in the source database to the target database.
    No changes from MaNGOS Zero to MaNGOS One.

    Args:
        cursor_source (mysql.connector.cursor.Cursor): Cursor for the source database.
        cursor_target (mysql.connector.cursor.Cursor): Cursor for the target database.
        new_db (mysql.connector.connection.MySQLConnection): Connection to the target database.

    Returns:
        None
    """
    table_name = "world"
    columns_to_copy = ["map", "data"]

    insert_query = f"INSERT INTO {table_name} ({','.join(columns_to_copy)}) VALUES ({','.join(['%s'] * len(columns_to_copy))})"
    cursor_source.execute(f"SELECT {','.join(columns_to_copy)} FROM {table_name}")
    rows = cursor_source.fetchall()

    progress_bar = tqdm(total=len(rows), desc=f"Migrating Data [{table_name}]")

    for row in rows:
        values = [row[column] for column in columns_to_copy]
        cursor_target.execute(insert_query, values)
        new_db.commit()
        progress_bar.update(1)  # Update progress bar

    # Close and clear progress bar
    progress_bar.close()
