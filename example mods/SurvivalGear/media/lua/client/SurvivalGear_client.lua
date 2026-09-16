-- media/lua/client/SurvivalGear_client.lua
local function onGameStart()
    print("[SurvivalGear] Survival Gear Mod v1.0.0 loaded successfully on Client.")
end

local function onFillInventoryObjectContextMenu(playerNum, context, items)
    local player = getSpecificPlayer(playerNum)
    if not player then return end

    for _, v in ipairs(items) do
        local item = v
        if not instanceof(item, "InventoryItem") then
            item = v.items[1]
        end

        if item and item:getFullType() == "SurvivalGear.TacticalCombatMachete" then
            context:addOption(getText("ContextMenu_InspectWeapon"), item, function(weapon)
                local cond = weapon:getCondition()
                local maxCond = weapon:getConditionMax()
                player:Say("Weapon Condition: " .. tostring(cond) .. " / " .. tostring(maxCond))
            end)
        end
    end
end

Events.OnGameStart.Add(onGameStart)
Events.OnFillInventoryObjectContextMenu.Add(onFillInventoryObjectContextMenu)
