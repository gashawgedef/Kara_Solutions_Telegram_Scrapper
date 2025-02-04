-- WITH telegram_data AS (
--     SELECT 
--         id, 
--         channel_title,
--         channel_username,
--         message_id,
--         message, 
--         -- created_at::timestamp, 
--         LENGTH(message) AS message_length
--     FROM public.telegram_messages
-- )
-- SELECT * FROM telegram_data
WITH telegram_data AS (
    SELECT 
        id, 
        channel_title,
        channel_username,
        message_id,
        convert_from(message::bytea, 'UTF8') AS message,  -- Decode message properly
        LENGTH(message) AS message_length
    FROM public.telegram_messages
)
SELECT * FROM telegram_data
