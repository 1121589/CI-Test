
#include "applications/app2/src/even_number.h"
#include "applications/app2/test/unity/unity.h"

/* sometimes you may want to get at local data in a module.
 * for example: If you plan to pass by reference, this could be useful
 * however, it should often be avoided */

void setUp(void)
{
  /* This is run before EACH TEST */
}

void tearDown(void)
{
}

void test_is_pair(void)
{
  /* All of these should pass */
  TEST_ASSERT_TRUE(is_number_even(2));
}

void test_is_not_pair(void)
{
  /* All of these should pass */
  TEST_ASSERT_FALSE(is_number_even(1));
}
