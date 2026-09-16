# Project Zomboid Lua Scripting Guide (Build 42 / 40.20.4)

## Architecture: Client, Server, and Shared

Lua code in Project Zomboid is divided into three scopes based on folder location:

1. **`media/lua/shared/`**:
   - Executes on **both** the client and server.
   - Used for game constants, item use callbacks, craft recipe callbacks, and shared data classes.
2. **`media/lua/client/`**:
   - Executes **only** on the local game client.
   - Used for UI windows, rendering hooks, world context menus, keypress handlers, and local sound triggers.
3. **`media/lua/server/`**:
   - Executes **only** on the server (or singleplayer host).
   - Used for authoritative inventory changes, zombie spawn control, weather modifications, and multiplayer command handlers.

## Standard Event Hooks

### 1. Adding Right-Click World Context Menu (`client`)
```lua
-- media/lua/client/ContextMenu/MyMod_WorldMenu.lua

local function onFillWorldObjectContextMenu(playerNum, context, worldObjects, test)
    if test then return true end
    
    local player = getSpecificPlayer(playerNum)
    if not player then return end

    -- Check if player clicked a valid target
    local clickedObject = nil
    for _, obj in ipairs(worldObjects) do
        if instanceof(obj, "IsoObject") then
            clickedObject = obj
            break
        end
    end

    if clickedObject then
        context:addOption(getText("ContextMenu_InspectObject"), clickedObject, function(obj)
            player:Say("This object looks sturdy.")
        end)
    end
end

Events.OnFillWorldObjectContextMenu.Add(onFillWorldObjectContextMenu)
```

### 2. Adding Inventory Context Menu (`client`)
```lua
-- media/lua/client/ContextMenu/MyMod_InventoryMenu.lua

local function onFillInventoryObjectContextMenu(playerNum, context, items)
    local player = getSpecificPlayer(playerNum)
    for _, v in ipairs(items) do
        local item = v
        if not instanceof(item, "InventoryItem") then
            item = v.items[1]
        end
        
        if item and item:getFullType() == "MyMod.TacticalCombatKnife" then
            context:addOption(getText("ContextMenu_CleanKnife"), item, function(knife)
                player:Say("Knife sharpened and cleaned.")
            end)
        end
    end
end

Events.OnFillInventoryObjectContextMenu.Add(onFillInventoryObjectContextMenu)
```

### 3. Safe Client-Server Networking
Never mutate global game state or spawn items authoritative-side from `client/` scripts in multiplayer. Use `sendClientCommand` and `OnClientCommand`:

```lua
-- Client side: send request to server
sendClientCommand(player, "MyMod", "CraftSpecialItem", { itemType = "MyMod.SpecialItem" })

-- Server side (media/lua/server/MyMod_Server.lua):
local function onClientCommand(module, command, player, args)
    if module ~= "MyMod" then return end
    if command == "CraftSpecialItem" then
        local inv = player:getInventory()
        inv:AddItem(args.itemType)
        sendServerCommand(player, "MyMod", "CraftSpecialItemSuccess", {})
    end
end

Events.OnClientCommand.Add(onClientCommand)
```

## Best Practices
- Always check `if not player then return end` inside event handlers.
- Use `getText("TranslationKey")` for user-facing strings instead of hardcoded strings.
- Keep tick events (`OnTick`) minimal to preserve framerate and avoid tick stutter.
