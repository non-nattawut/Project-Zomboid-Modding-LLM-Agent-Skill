-- media/lua/client/MyMod_Client.lua

local function onGameStart()
    print("[MyMod] Client initialized for Build 42 / 40.20.4")
end

local function onFillInventoryObjectContextMenu(playerNum, context, items)
    local player = getSpecificPlayer(playerNum)
    if not player then return end

    for _, v in ipairs(items) do
        local item = v
        if not instanceof(item, "InventoryItem") then
            item = v.items[1]
        end

        if item and item:getFullType() == "MyMod.CustomMachete" then
            context:addOption(getText("ContextMenu_InspectWeapon"), item, function(targetItem)
                player:Say("This blade is forged for survival.")
            end)
        end
    end
end

Events.OnGameStart.Add(onGameStart)
Events.OnFillInventoryObjectContextMenu.Add(onFillInventoryObjectContextMenu)
