from fonction_math import async_function
import pytest

@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == 42
