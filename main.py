from speech import listen
from parser import parse_command
from devices import SmartHome

home = SmartHome()

print("\n===== SMART HOME AUTOMATION =====")
print("Voice Commands:")
print("- Turn on light")
print("- Turn off light")
print("- Turn on fan")
print("- Turn off fan")
print("- Turn on AC")
print("- Turn off AC")
print()

while True:

    home.show_status()

    text = listen()

    if text is None:
        continue

    command = parse_command(text)

    if command:

        print(f"\n✅ Command Detected: {command}")

        # Update terminal status
        home.execute(command)

        # Send command to Webots
        with open("command.txt", "w") as f:
            f.write(command)

    else:

        print("\n❌ Command not recognized.")

    print()