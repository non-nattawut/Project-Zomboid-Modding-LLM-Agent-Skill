-- media/lua/server/SurvivalGear_server.lua
local function onClientCommand(module, command, player, args)
    if module ~= "SurvivalGear" then return end
    -- Server authoritative handling if needed
end

Events.OnClientCommand.Add(onClientCommand)
