import asyncio
from leds import Leds
from debug import set_global_exception

async def main():
    set_global_exception()
    lit = Leds()
    await asyncio.create_task(lit.dance())
    # await leds.run_forever()  # Non-terminating method
try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()  # Clear retained state