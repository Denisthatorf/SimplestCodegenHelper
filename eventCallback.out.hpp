#pragma once

namespace irl
{
    class f_eventCallback_int_float_float
	{
	typedef int (*functor_t)( float x, float y );

    public:
        f_eventCallback_int_float_float (functor_t functor)
            : functionPtr  (functor) {}

        f_eventCallback_int_float_float() = default;

        int operator() ( float x, float y ) const
        {
            return functionPtr( x, y );
        }

        functor_t functionPtr = nullptr;
    };
    class f_eventCallback_int_double_double
	{
	typedef int (*functor_t)( double x, double y );

    public:
        f_eventCallback_int_double_double (functor_t functor)
            : functionPtr  (functor) {}

        f_eventCallback_int_double_double() = default;

        int operator() ( double x, double y ) const
        {
            return functionPtr( x, y );
        }

        functor_t functionPtr = nullptr;
    };
    class f_eventCallback_int_int_int
	{
	typedef int (*functor_t)( int x, int y );

    public:
        f_eventCallback_int_int_int (functor_t functor)
            : functionPtr  (functor) {}

        f_eventCallback_int_int_int() = default;

        int operator() ( int x, int y ) const
        {
            return functionPtr( x, y );
        }

        functor_t functionPtr = nullptr;
    };
} // namespace irl
