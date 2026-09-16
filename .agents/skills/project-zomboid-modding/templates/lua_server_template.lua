-- media/lua/server/MyMod_Server.lua

local function onClientCommand(module, command, player, args)
    if module ~= "MyMod" then return end

    if command == "RequestCraftingReward" then
        local inv = player:getInventory()
        if inv then
            inv:AddItem("MyMod.CustomMaterial")
            sendServerCommand(player, "MyMod", "CraftingRewardGranted", { success = true })
        end
    end
end

Events.OnClientCommand.Add(onClientCommand)
